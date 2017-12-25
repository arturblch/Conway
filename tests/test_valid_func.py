import pytest

from Strategy_new import Strategy
from util.WorldGetter import WorldGetter
from model.Player import Player
from model.Map import Map, Position
from model.Objects import Objects
from pprint import pprint

from algo.WCA import WCAStar


def test_valid():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)
    strategy.get_invalid_pos = lambda x: {}

    reserv_pos = {
        1: {
            0: Position(None, 1, 3),
            1: Position(2),
            2: Position(None, 12, 1)
        },
        2: {
            0: Position(None, 2, 2),
            1: Position(None, 2, 1),
            2: Position(None, 2, 2)
        }
    }

    strategy.trains_reservations = reserv_pos
    train = objects.trains[1]
    print(strategy.valid(train, Position(None, 1, 1), Position(1)))