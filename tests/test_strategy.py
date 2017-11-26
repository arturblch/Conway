import pytest
import json
from Strategy import Strategy
from model.World import World
from model.Game import Game
from model.Move import Move

start_data = json.loads(
    '''{
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
}''')

game_responce = json.loads(
'''{
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
 }''')

world_responce = json.loads(
'''{
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
            "speed": 0
        }
    ]
}''')


world = World(posts=world_responce['post'], trains=world_responce['train'])
game = Game(lines=game_responce['line'], points=game_responce['point'])

def test_defult():

    strategy = Strategy(start_data)
    next_move = strategy.move(world, game)

    print(next_move)
    test_move = Move(12,1,0)
    assert next_move.line_idx == test_move.line_idx
    assert next_move.speed == test_move.speed
    assert next_move.train_idx == test_move.train_idx


