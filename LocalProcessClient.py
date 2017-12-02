import json
import logging
import os
clear = lambda: os.system('cls')
from time import sleep
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

        return deepcopy(self.player)

    def turn(self):
        os.system('cls')
        for train in self.objects.trains.values():
            if not self.check_speed(train):
                train.speed = 0
            train.position += train.speed
            clear()
            print(
                tabulate(
                    [[train.idx, train.line_idx, train.speed, train.position]],
                    headers=['Train_id', 'line_idx', 'speed', 'position']))
        sleep(0.5)

    def move(self, move):
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

    def update_trains_node(self):
        self.objects.update_trains(self.map.lines)

    def read_objects(self):
        self.update_trains_node()
        return deepcopy(self.objects)

    def read_map(self):
        return deepcopy(self.map)

    def check_speed(self, train):
        if 0 <= train.position + train.speed <= self.map.lines[train.
                                                             line_idx].length:
            return True
        return False
