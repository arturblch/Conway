import sys
sys.path.append('../')


from enum import IntEnum
from util.WorldGetter import WorldGetter
from model.Player import Player
from model.Map import Map
from model.Objects import Objects

from LocalProcessClient import LocalProcessClient

class World:
    def __init__(self, player, map_, objects):
        self.player = player
        self.map = map_
        self.objects = objects
        self.tick_ = 0

        self.process_client = LocalProcessClient(player, map_, objects)

    def next_tick(self):
        self.tick_ +=1 
        self.process_client.turn()

    def tick(self):
        return self.tick_

    def my_trains(self):
        return self.objects.trains

    def get_parts(self):
        return (self.player, self.map, self.objects)


class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class direction(IntEnum):
    north = 0
    east = 1
    south = 2
    west = 3


def translate(p, d):
    if d is direction.north:
        return [p.x, p.y - 1]
    elif d is direction.east:
        return [p.x + 1, p.y]
    elif d is direction.south:
        return [p.x, p.y + 1]
    elif d is direction.west:
        return [p.x - 1, p.y]
    raise ValueError("Unreachable")
    return None

def in_bounds(pos, map_):
    return (pos.x >= 0 and
            pos.y >= 0 and
            pos.x < map_.width() and
            pos.y < map_.height())



def get_world():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_ = Map(factory.get_map())
    map_.pos = factory.get_pos()
    objects = Objects(factory.get_objects())


    return World(player, map_, objects)