import pytest
from model.Map import Map, Position
from util.WorldGetter import WorldGetter


def test_correct_init():
    factory = WorldGetter(3)

    map_graph = Map(factory.get_map())


def test_get_neighbors_pos():

    factory = WorldGetter(3)
    map_graph = Map(factory.get_map())

    pos = Position(None, 2, 1)
    assert(map_graph.get_neighbors_pos(pos) == [Position(2), Position(None, 2,2)])
