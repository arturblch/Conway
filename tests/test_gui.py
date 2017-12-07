from GUI import GUI
from util.WorldGetter import WorldGetter
from model.Map import Map
from model.Objects import Objects
from model.Player import Player

import json


def test_base():
    factory = WorldGetter(3)
    _map = Map(factory.get_map())
    _map.pos = factory.get_pos()
    objects = Objects(factory.get_objects())
    player = Player(factory.get_player())
    i = 30
    gui = GUI(player, _map, objects)
    gui.fps = 30
    gui.paused = True
    while player.is_alive:
        gui.turn()
        if gui.paused == False:
            objects.trains[1].line_idx = 1
            if objects.trains[1].position == 4:
                objects.trains[1].speed = -1
            elif objects.trains[1].position == 0:
                objects.trains[1].speed = 1
            objects.trains[1].position += objects.trains[1].speed
            objects.trains[1].line_idx = 10
            if objects.trains[2].position == 5:
                objects.trains[2].speed = -1
            elif objects.trains[2].position == 0:
                objects.trains[2].speed = 1
            objects.trains[2].position += objects.trains[2].speed
            if i > 0:
                i -= 1
            else:
                player.is_alive = False

    gui.close()
