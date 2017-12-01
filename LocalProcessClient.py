import json
import logging
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
formatter = logging.Formatter(
    '%(asctime)s - %(message)s')
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

        logger.info("Init world")

    def login(self):
        factory = WorldGetter(1)
        self.map = Map(factory.get_map())
        self.objects = Objects(factory.get_objects())
        self.player = Player(factory.get_player())

        return deepcopy(self.player)

    def turn(self):
        return self.write_message('TURN')

    def read_objects(self):
        layer = self.write_message('MAP', {"layer": 1})[1]
        return Objects(layer)

    def update_objects(self, objects):
        layer = self.write_message('MAP', {"layer": 1})[1]
        objects.update(layer)

    def read_map(self):
        layer = self.write_message('MAP', {"layer": 0})[1]
        return Map(layer)
