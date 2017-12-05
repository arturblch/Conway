from GUI import GUI
from util.WorldGetter import WorldGetter
from model.Map import Map
from model.Objects import Objects
from model.Player import Player

import json


def test_base():
    factory = WorldGetter(3)
    _map = Map(factory.get_map())
    objects = Objects(factory.get_objects())
    player = Player(factory.get_player())
    i = 30
    gui = GUI(player, _map, objects)
    gui.fps = 30
    gui.paused = False
    while player.is_alive:
        gui.turn()
        if gui.paused == False:
            if objects.trains[0].position == 10:
                objects.trains[0].speed = -1
            elif objects.trains[0].position == 0:
                objects.trains[0].speed = 1
            objects.trains[0].position += objects.trains[0].speed
            if i > 0:
                i -= 1
            else:
                player.is_alive = False

    gui.close()
