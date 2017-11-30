from GUI import GUI
from model.Player import Player
from model.Map import Map
from model.Objects import Objects
import json

player =  Player(json.loads('''{
    "home": {
        "idx": 1,
        "post_id": 1
    },
    "idx": "dcdfdf83-cbcf-4cec-8ad8-c919c7f6781d",
    "name": "Mickey",
    "train": [
        {
            "capacity": 15,
            "idx": 0,
            "line_idx": null,
            "player_id": "dcdfdf83-cbcf-4cec-8ad8-c919c7f6781d",
            "position": null,
            "product": 0,
            "speed": 0
        }
    ]
}'''))


objects = Objects(json.loads('''{
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
            "idx": 2,
            "name": "market-one",
            "product": 20,
            "type": 2
        }
    ],
    "train": [
        {
            "capacity": 15,
            "idx": 0,
            "line_idx": 1,
            "player_id": "dcdfdf83-cbcf-4cec-8ad8-c919c7f6781d",
            "position": 10,
            "product": 0,
            "speed": 1
        }
    ]
}'''))

map_graph = Map(json.loads('''{
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

def test_base:
    gui = GUI(map_graph, objects)
    while strategy.in_progress:
        self.remote_process_client.update_objects(strategy.objects)

        moves = strategy.get_moves()
        if moves:
            for move in moves:
                self.remote_process_client.move(move)
        if self.is_gui:
            self.gui.turn()
        self.remote_process_client.turn()
