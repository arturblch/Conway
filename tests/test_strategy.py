import pytest

from Strategy_new import Strategy
from util.WorldGetter import WorldGetter
from model.Player import Player
from model.Map import Map, Position
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


def test_upgrade_targets():

    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)

    assert(strategy.trains_points == {1: [], 2: []})
    strategy.update_targets()
    assert(strategy.trains_points == {1: [12, 1], 2: [32, 1]})

def test_get_invalid_pos():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)
    

    train = objects.trains[1]
    invalid = [Position(None, 11, 2),
               Position(None, 11, 4),
               Position(None, 11, 3),
               Position(32),
               Position(56)]
    assert(strategy.get_invalid_pos(train) == invalid)


def test_find_path():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)
    path = [Position(1, 1, 0),
               Position(None, 1, 1),
               Position(None, 1, 2),
               Position(None, 1, 3)]
    assert(strategy.find_path(1, Position(33)) == path )

def test_recalculate():
    factory = WorldGetter(3)

    player = Player(factory.get_player())
    map_graph = Map(factory.get_map())
    objects = Objects(factory.get_objects())

    strategy = Strategy(player, map_graph, objects)
    strategy.trains_points[1] = [33]
    strategy.trains_points[2] = [29]

    print(strategy.recalculate(1))
    print(strategy.recalculate(2))
