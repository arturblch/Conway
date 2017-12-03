import json
import logging
from tabulate import tabulate
from copy import deepcopy
from model.Objects import Objects
from model.Map import Map
from model.Player import Player
from util.WorldGetter import WorldGetter

# create logger
logger = logging.getLogger('LocalProcessClient')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('LocalProcessClient.log')
fh.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


class ProcessClient:
    def __init__(self):
        self.player = None
        self.map = None
        self.objects = None

    def login(self, world=1):
        factory = WorldGetter(world)
        # create template objects
        self.map = Map(factory.get_map())
        self.objects = Objects(factory.get_objects())
        self.player = Player(factory.get_player())
        self.init_train()
        logger.info("Login")

        return self.player

    def init_train(self):
        for train in self.objects.trains.values():
            train.node = self.player.home.idx

    def turn_trains(self):
        for train in self.objects.trains.values():
            if train.line_idx != None:
                if not self.check_speed(train, train.speed):
                    train.speed = 0
                train.position += train.speed
                train.update_node(self.map.lines)
                if train.node:
                    post_id = self.map.points[train.node].post_id
                    if post_id:
                        if post_id in self.objects.towns.keys():
                            self.objects.towns[
                                post_id].product += train.product
                            train.product = 0
                        elif post_id in self.objects.markets.keys():
                            train.product += self.objects.markets[
                                post_id].product
                            self.objects.markets[post_id].product = 0

    def turn_markets(self):
        for market in self.objects.markets.values():
            if market.product < market.product_capacity:
                market.product += market.replenishment

    def turn_towns(self):
        for town in self.objects.towns.values():
            if town.product < town.population:
                town.population -= 1
            town.product = (town.product - town.population
                            if town.product - town.population > 0 else 0)

    def print_state(self):
        str_post = []
        for town in self.objects.towns.values():
            str_post.append([town.name, town.product, town.population])
        for market in self.objects.markets.values():
            str_post.append([market.name, market.product, '-'])

        print(
            tabulate(str_post, headers=['name', 'products', 'population']),
            '\n')

        for train in self.objects.trains.values():
            print(
                tabulate(
                    [[
                        train.idx, train.product, train.line_idx, train.speed,
                        train.position
                    ]],
                    headers=[
                        'Train_id', 'product', 'line_idx', 'speed', 'position'
                    ]))

    def turn(self):
        self.turn_markets()
        self.turn_trains()
        self.turn_towns()
        self.print_state()

    def move(self, move):
        logger.info(move)
        if move.train_idx in self.objects.trains.keys():
            train = self.objects.trains[move.train_idx]
            if move.line_idx in self.map.lines.keys():
                if move.line_idx == train.line_idx:
                    if self.check_speed(train, move.speed):
                        train.speed = move.speed
                line = self.map.lines[move.line_idx]
                if train.node == line.start_point:
                    train.line_idx = move.line_idx
                    if self.check_speed(train, move.speed):
                        train.speed = move.speed
                    train.position = 0

                if train.node == line.end_point:
                    train.line_idx = move.line_idx
                    if self.check_speed(train, move.speed):
                        train.speed = move.speed
                    train.position = line.length

    def read_objects(self):
        return self.objects

    def read_map(self):
        return self.map

    def check_speed(self, train, speed):
        if 0 <= train.position + speed <= self.map.lines[train.line_idx].length:
            return True
        return False
