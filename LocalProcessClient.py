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
        logger.info("Login")

        return self.player

    def turn(self):
        for train in self.objects.trains.values():
            if not self.check_speed(train):
                train.speed = 0
            train.position += train.speed
            train.update_node(self.map.lines)
            print(
                tabulate(
                    [[train.idx, train.line_idx, train.speed, train.position]],
                    headers=['Train_id', 'line_idx', 'speed', 'position']))

    def move(self, move):
        logger.info(move)
        if move.train_idx in self.objects.trains.keys():
            train = self.objects.trains[move.train_idx]
            if move.line_idx in self.map.lines.keys():
                if move.line_idx == train.line_idx:
                    train.speed = move.speed
                line = self.map.lines[move.line_idx]
                if train.node == line.start_point:
                    train.line_idx = move.line_idx
                    train.speed = move.speed
                    train.position = 0

                if train.node == line.end_point:
                    train.line_idx = move.line_idx
                    train.speed = move.speed
                    train.position = line.length

    def read_objects(self):
        return self.objects

    def read_map(self):
        return self.map

    def check_speed(self, train):
        if 0 <= train.position + train.speed <= self.map.lines[train.
                                                             line_idx].length:
            return True
        return False
