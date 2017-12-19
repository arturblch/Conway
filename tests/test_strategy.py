import pytest

from Strategy_new import Strategy
from util.WorldGetter import WorldGetter
from model.Player import Player
from model.Map import Map
from model.Objects import Objects



def test_correct_init():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)


def test_get_up_object():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)

    objects.towns[1].armor = 141
    strategy._get_up_object()
    assert (strategy.up_object.post == [1] and
           strategy.up_object.train == [])

    objects.towns[1].armor = 100
    strategy._get_up_object()
    assert (strategy.up_object.post == [] and
           strategy.up_object.train == [1])

    objects.towns[1].armor = 500
    strategy._get_up_object()
    assert (strategy.up_object.post == [1] and
            strategy.up_object.train == [1, 2])

def test_get_target_points():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)

    train = objects.trains[1]
    strategy._get_target_points(train)
    assert(strategy.trains_points[1] == [12, 1])

    train.goods_capacity = 160
    strategy._get_target_points(train)
    assert(strategy.trains_points[1] == [49, 1])

    # print([(market.product, market.point, map_graph.get_distance(1, market.point)) for market in strategy.objects.markets.values()])

def test_move_to_point():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)

    train = objects.trains[1]

    move = strategy._move_to_point(train, 11)
    print(move)