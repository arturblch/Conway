import json

class WorldGetter:
    player = json.loads('''{
        "home": {
            "idx": 1,
            "post_id": 1
        },
        "idx": "082309a9-354d-4673-9533-b97fdf9a042a",
        "name": "Mickey",
        "town": {
            "armor": 0,
            "idx": 1,
            "name": "town-one",
            "population": 3,
            "product": 35,
            "type": 1
        },
        "train": [
            {
                "capacity": 200,
                "idx": 0,
                "line_idx": null,
                "player_id": "082309a9-354d-4673-9533-b97fdf9a042a",
                "position": null,
                "product": 0,
                "speed": 0
            }
        ]
    }''')

    map01 = json.loads('''{
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

    map02 = json.loads('''{
        "idx": 1,
        "line": [
            {
                "idx": 1,
                "length": 1,
                "point": [
                    1,
                    7
                ]
            },
            {
                "idx": 2,
                "length": 1,
                "point": [
                    8,
                    2
                ]
            },
            {
                "idx": 3,
                "length": 1,
                "point": [
                    9,
                    3
                ]
            },
            {
                "idx": 4,
                "length": 1,
                "point": [
                    10,
                    4
                ]
            },
            {
                "idx": 5,
                "length": 1,
                "point": [
                    11,
                    5
                ]
            },
            {
                "idx": 6,
                "length": 2,
                "point": [
                    12,
                    6
                ]
            },
            {
                "idx": 7,
                "length": 1,
                "point": [
                    7,
                    8
                ]
            },
            {
                "idx": 8,
                "length": 2,
                "point": [
                    8,
                    9
                ]
            },
            {
                "idx": 9,
                "length": 2,
                "point": [
                    9,
                    10
                ]
            },
            {
                "idx": 10,
                "length": 1,
                "point": [
                    10,
                    11
                ]
            },
            {
                "idx": 11,
                "length": 3,
                "point": [
                    11,
                    12
                ]
            },
            {
                "idx": 12,
                "length": 1,
                "point": [
                    12,
                    7
                ]
            },
            {
                "idx": 13,
                "length": 2,
                "point": [
                    1,
                    2
                ]
            },
            {
                "idx": 14,
                "length": 2,
                "point": [
                    2,
                    3
                ]
            },
            {
                "idx": 15,
                "length": 1,
                "point": [
                    3,
                    4
                ]
            },
            {
                "idx": 16,
                "length": 3,
                "point": [
                    4,
                    5
                ]
            },
            {
                "idx": 17,
                "length": 1,
                "point": [
                    5,
                    6
                ]
            },
            {
                "idx": 18,
                "length": 3,
                "point": [
                    6,
                    1
                ]
            }
        ],
        "name": "map02",
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
                "post_id": 2
            },
            {
                "idx": 5,
                "post_id": 3
            },
            {
                "idx": 6,
                "post_id": null
            },
            {
                "idx": 7,
                "post_id": 4
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

    objects01 = json.loads('''{
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
                "product_capacity" : 20,
                "replenishment" : 1,
                "type": 2
            }
        ],
        "train": [
            {
                "capacity": 15,
                "idx": 0,
                "line_idx": 1,
                "player_id": "1867fde9-5c0d-4db8-9b71-e0145832e4d4",
                "position": 0,
                "product": 0,
                "speed": 0
            }
        ]
    }''')

    objects02 =  json.loads('''{
        "idx": 1,
        "post": [
            {
                "armor": 0,
                "idx": 1,
                "name": "town-one",
                "population": 3,
                "product": 35,
                "type": 1
            },
            {
                "idx": 2,
                "name": "market-big",
                "product": 36,
                "product_capacity": 36,
                "replenishment": 2,
                "type": 2
            },
            {
                "idx": 3,
                "name": "market-medium",
                "product": 28,
                "product_capacity": 28,
                "replenishment": 1,
                "type": 2
            },
            {
                "idx": 4,
                "name": "market-small",
                "product": 5,
                "product_capacity": 5,
                "replenishment": 1,
                "type": 2
            }
        ],
        "train": [
            {
                "capacity": 200,
                "idx": 0,
                "line_idx": 1,
                "player_id": "082309a9-354d-4673-9533-b97fdf9a042a",
                "position": 0,
                "product": 0,
                "speed": 0
            }
        ]
    }''')

    
    def __init__(self, num=1):
        self.num = num

    def get_map(self):
        return getattr(self, "map%02d" % self.num)

    def get_objects(self):
        return getattr(self, "objects%02d" % self.num)

    def get_player(self):
        return self.player
