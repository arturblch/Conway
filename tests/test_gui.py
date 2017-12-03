from GUI import GUI
from model.Map import Map
from model.Objects import Objects

import json


class Player:
    def __init__(self):
        self.is_alive = True


player = Player()

objects = Objects(
    json.loads('''{
"idx": 1,
    "post": [
        {
            "armor": 0,
            "idx": 1,
            "name": "town-one",
            "population": 10,
            "product": 0,
            "type": 1
        },
        {
            "product_capacity": 20,
            "replenishment" : 5,
            "idx": 2,
            "name": "market-one",
            "product": 20,
            "type": 2
        }
    ],
    "train": [
        {
            "product_capacity": 20,
            "capacity": 15,
            "idx": 0,
            "line_idx": 1,
            "player_id": "dcdfdf83-cbcf-4cec-8ad8-c919c7f6781d",
            "position": 0,
            "product": 0,
            "speed": 1
        }
    ]
}'''))

map_graph = Map(
    json.loads('''{
    "idx": 1,
    "line": [
        {
            "idx": 1,
            "length": 10,
            "point": [
                1,
                7
            ]
        },
        {
            "idx": 2,
            "length": 10,
            "point": [
                8,
                2
            ]
        },
        {
            "idx": 3,
            "length": 10,
            "point": [
                9,
                3
            ]
        },
        {
            "idx": 4,
            "length": 10,
            "point": [
                10,
                4
            ]
        },
        {
            "idx": 5,
            "length": 10,
            "point": [
                11,
                5
            ]
        },
        {
            "idx": 6,
            "length": 10,
            "point": [
                12,
                6
            ]
        },
        {
            "idx": 7,
            "length": 10,
            "point": [
                7,
                8
            ]
        },
        {
            "idx": 8,
            "length": 10,
            "point": [
                8,
                9
            ]
        },
        {
            "idx": 9,
            "length": 10,
            "point": [
                9,
                10
            ]
        },
        {
            "idx": 10,
            "length": 10,
            "point": [
                10,
                11
            ]
        },
        {
            "idx": 11,
            "length": 10,
            "point": [
                11,
                12
            ]
        },
        {
            "idx": 12,
            "length": 10,
            "point": [
                12,
                7
            ]
        }
    ],
    "name": "map01",
    "point": [
        {
            "idx": 1,
            "post_id": 1
        },
        {
            "idx": 2,
            "post_id": null
        },
        {
            "idx": 3,
            "post_id": null
        },
        {
            "idx": 4,
            "post_id": null
        },
        {
            "idx": 5,
            "post_id": null
        },
        {
            "idx": 6,
            "post_id": null
        },
        {
            "idx": 7,
            "post_id": 2
        },
        {
            "idx": 8,
            "post_id": null
        },
        {
            "idx": 9,
            "post_id": null
        },
        {
            "idx": 10,
            "post_id": null
        },
        {
            "idx": 11,
            "post_id": null
        },
        {
            "idx": 12,
            "post_id": null
        }
    ]
}'''))


def test_base():
    i = 30
    gui = GUI(player, map_graph, objects)
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
            if i>0:
                i-=1
            else:
                player.is_alive = False

    gui.close()
