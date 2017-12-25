import json


class WorldGetter:
    player = json.loads('''{
    "home": {
        "idx": 1,
        "post_id": 1
    },
    "idx": "07f32b23-8127-49f5-ab65-be7d5c775d6a",
    "name": "Test_Conway",
    "town": {
        "armor": 100,
        "armor_capacity": 100,
        "event": [],
        "idx": 1,
        "level": 1,
        "name": "town-one",
        "next_level_price": 100,
        "player_id": "07f32b23-8127-49f5-ab65-be7d5c775d6a",
        "point_id": 1,
        "population": 3,
        "population_capacity": 10,
        "product": 350,
        "product_capacity": 200,
        "type": 1
    },
    "train": [
        {
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 1,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "07f32b23-8127-49f5-ab65-be7d5c775d6a",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 2,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "07f32b23-8127-49f5-ab65-be7d5c775d6a",
            "position": 0,
            "post_type": null,
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

    objects02 = json.loads('''{
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

    map03 = json.loads('''{
        "idx": 1,
        "line": [
            {
                "idx": 1,
                "length": 4,
                "point": [
                    1,
                    2
                ]
            },
            {
                "idx": 2,
                "length": 4,
                "point": [
                    2,
                    3
                ]
            },
            {
                "idx": 3,
                "length": 4,
                "point": [
                    3,
                    4
                ]
            },
            {
                "idx": 4,
                "length": 4,
                "point": [
                    4,
                    5
                ]
            },
            {
                "idx": 5,
                "length": 4,
                "point": [
                    5,
                    6
                ]
            },
            {
                "idx": 6,
                "length": 4,
                "point": [
                    6,
                    7
                ]
            },
            {
                "idx": 7,
                "length": 4,
                "point": [
                    7,
                    8
                ]
            },
            {
                "idx": 8,
                "length": 4,
                "point": [
                    8,
                    9
                ]
            },
            {
                "idx": 9,
                "length": 4,
                "point": [
                    9,
                    10
                ]
            },
            {
                "idx": 10,
                "length": 5,
                "point": [
                    1,
                    11
                ]
            },
            {
                "idx": 11,
                "length": 5,
                "point": [
                    2,
                    12
                ]
            },
            {
                "idx": 12,
                "length": 5,
                "point": [
                    3,
                    13
                ]
            },
            {
                "idx": 13,
                "length": 5,
                "point": [
                    4,
                    14
                ]
            },
            {
                "idx": 14,
                "length": 5,
                "point": [
                    5,
                    15
                ]
            },
            {
                "idx": 15,
                "length": 5,
                "point": [
                    6,
                    16
                ]
            },
            {
                "idx": 16,
                "length": 5,
                "point": [
                    7,
                    17
                ]
            },
            {
                "idx": 17,
                "length": 5,
                "point": [
                    8,
                    18
                ]
            },
            {
                "idx": 18,
                "length": 5,
                "point": [
                    9,
                    19
                ]
            },
            {
                "idx": 19,
                "length": 5,
                "point": [
                    10,
                    20
                ]
            },
            {
                "idx": 20,
                "length": 4,
                "point": [
                    11,
                    12
                ]
            },
            {
                "idx": 21,
                "length": 4,
                "point": [
                    12,
                    13
                ]
            },
            {
                "idx": 22,
                "length": 4,
                "point": [
                    13,
                    14
                ]
            },
            {
                "idx": 23,
                "length": 4,
                "point": [
                    14,
                    15
                ]
            },
            {
                "idx": 24,
                "length": 4,
                "point": [
                    15,
                    16
                ]
            },
            {
                "idx": 25,
                "length": 4,
                "point": [
                    16,
                    17
                ]
            },
            {
                "idx": 26,
                "length": 4,
                "point": [
                    17,
                    18
                ]
            },
            {
                "idx": 27,
                "length": 4,
                "point": [
                    18,
                    19
                ]
            },
            {
                "idx": 28,
                "length": 4,
                "point": [
                    19,
                    20
                ]
            },
            {
                "idx": 29,
                "length": 5,
                "point": [
                    11,
                    21
                ]
            },
            {
                "idx": 30,
                "length": 5,
                "point": [
                    12,
                    22
                ]
            },
            {
                "idx": 31,
                "length": 5,
                "point": [
                    13,
                    23
                ]
            },
            {
                "idx": 32,
                "length": 5,
                "point": [
                    14,
                    24
                ]
            },
            {
                "idx": 33,
                "length": 5,
                "point": [
                    15,
                    25
                ]
            },
            {
                "idx": 34,
                "length": 5,
                "point": [
                    16,
                    26
                ]
            },
            {
                "idx": 35,
                "length": 5,
                "point": [
                    17,
                    27
                ]
            },
            {
                "idx": 36,
                "length": 5,
                "point": [
                    18,
                    28
                ]
            },
            {
                "idx": 37,
                "length": 5,
                "point": [
                    19,
                    29
                ]
            },
            {
                "idx": 38,
                "length": 5,
                "point": [
                    20,
                    30
                ]
            },
            {
                "idx": 39,
                "length": 4,
                "point": [
                    21,
                    22
                ]
            },
            {
                "idx": 40,
                "length": 4,
                "point": [
                    22,
                    23
                ]
            },
            {
                "idx": 41,
                "length": 4,
                "point": [
                    23,
                    24
                ]
            },
            {
                "idx": 42,
                "length": 4,
                "point": [
                    24,
                    25
                ]
            },
            {
                "idx": 43,
                "length": 4,
                "point": [
                    25,
                    26
                ]
            },
            {
                "idx": 44,
                "length": 4,
                "point": [
                    26,
                    27
                ]
            },
            {
                "idx": 45,
                "length": 4,
                "point": [
                    27,
                    28
                ]
            },
            {
                "idx": 46,
                "length": 4,
                "point": [
                    28,
                    29
                ]
            },
            {
                "idx": 47,
                "length": 4,
                "point": [
                    29,
                    30
                ]
            },
            {
                "idx": 48,
                "length": 5,
                "point": [
                    21,
                    31
                ]
            },
            {
                "idx": 49,
                "length": 5,
                "point": [
                    22,
                    32
                ]
            },
            {
                "idx": 50,
                "length": 5,
                "point": [
                    23,
                    33
                ]
            },
            {
                "idx": 51,
                "length": 5,
                "point": [
                    24,
                    34
                ]
            },
            {
                "idx": 52,
                "length": 5,
                "point": [
                    25,
                    35
                ]
            },
            {
                "idx": 53,
                "length": 5,
                "point": [
                    26,
                    36
                ]
            },
            {
                "idx": 54,
                "length": 5,
                "point": [
                    27,
                    37
                ]
            },
            {
                "idx": 55,
                "length": 5,
                "point": [
                    28,
                    38
                ]
            },
            {
                "idx": 56,
                "length": 5,
                "point": [
                    29,
                    39
                ]
            },
            {
                "idx": 57,
                "length": 5,
                "point": [
                    30,
                    40
                ]
            },
            {
                "idx": 58,
                "length": 4,
                "point": [
                    31,
                    32
                ]
            },
            {
                "idx": 59,
                "length": 4,
                "point": [
                    32,
                    33
                ]
            },
            {
                "idx": 60,
                "length": 4,
                "point": [
                    33,
                    34
                ]
            },
            {
                "idx": 61,
                "length": 4,
                "point": [
                    34,
                    35
                ]
            },
            {
                "idx": 62,
                "length": 4,
                "point": [
                    35,
                    36
                ]
            },
            {
                "idx": 63,
                "length": 4,
                "point": [
                    36,
                    37
                ]
            },
            {
                "idx": 64,
                "length": 4,
                "point": [
                    37,
                    38
                ]
            },
            {
                "idx": 65,
                "length": 4,
                "point": [
                    38,
                    39
                ]
            },
            {
                "idx": 66,
                "length": 4,
                "point": [
                    39,
                    40
                ]
            },
            {
                "idx": 67,
                "length": 5,
                "point": [
                    31,
                    41
                ]
            },
            {
                "idx": 68,
                "length": 5,
                "point": [
                    32,
                    42
                ]
            },
            {
                "idx": 69,
                "length": 5,
                "point": [
                    33,
                    43
                ]
            },
            {
                "idx": 70,
                "length": 5,
                "point": [
                    34,
                    44
                ]
            },
            {
                "idx": 71,
                "length": 5,
                "point": [
                    35,
                    45
                ]
            },
            {
                "idx": 72,
                "length": 5,
                "point": [
                    36,
                    46
                ]
            },
            {
                "idx": 73,
                "length": 5,
                "point": [
                    37,
                    47
                ]
            },
            {
                "idx": 74,
                "length": 5,
                "point": [
                    38,
                    48
                ]
            },
            {
                "idx": 75,
                "length": 5,
                "point": [
                    39,
                    49
                ]
            },
            {
                "idx": 76,
                "length": 5,
                "point": [
                    40,
                    50
                ]
            },
            {
                "idx": 77,
                "length": 4,
                "point": [
                    41,
                    42
                ]
            },
            {
                "idx": 78,
                "length": 4,
                "point": [
                    42,
                    43
                ]
            },
            {
                "idx": 79,
                "length": 4,
                "point": [
                    43,
                    44
                ]
            },
            {
                "idx": 80,
                "length": 4,
                "point": [
                    44,
                    45
                ]
            },
            {
                "idx": 81,
                "length": 4,
                "point": [
                    45,
                    46
                ]
            },
            {
                "idx": 82,
                "length": 4,
                "point": [
                    46,
                    47
                ]
            },
            {
                "idx": 83,
                "length": 4,
                "point": [
                    47,
                    48
                ]
            },
            {
                "idx": 84,
                "length": 4,
                "point": [
                    48,
                    49
                ]
            },
            {
                "idx": 85,
                "length": 4,
                "point": [
                    49,
                    50
                ]
            },
            {
                "idx": 86,
                "length": 5,
                "point": [
                    41,
                    51
                ]
            },
            {
                "idx": 87,
                "length": 5,
                "point": [
                    42,
                    52
                ]
            },
            {
                "idx": 88,
                "length": 5,
                "point": [
                    43,
                    53
                ]
            },
            {
                "idx": 89,
                "length": 5,
                "point": [
                    44,
                    54
                ]
            },
            {
                "idx": 90,
                "length": 5,
                "point": [
                    45,
                    55
                ]
            },
            {
                "idx": 91,
                "length": 5,
                "point": [
                    46,
                    56
                ]
            },
            {
                "idx": 92,
                "length": 5,
                "point": [
                    47,
                    57
                ]
            },
            {
                "idx": 93,
                "length": 5,
                "point": [
                    48,
                    58
                ]
            },
            {
                "idx": 94,
                "length": 5,
                "point": [
                    49,
                    59
                ]
            },
            {
                "idx": 95,
                "length": 5,
                "point": [
                    50,
                    60
                ]
            },
            {
                "idx": 96,
                "length": 4,
                "point": [
                    51,
                    52
                ]
            },
            {
                "idx": 97,
                "length": 4,
                "point": [
                    52,
                    53
                ]
            },
            {
                "idx": 98,
                "length": 4,
                "point": [
                    53,
                    54
                ]
            },
            {
                "idx": 99,
                "length": 4,
                "point": [
                    54,
                    55
                ]
            },
            {
                "idx": 100,
                "length": 4,
                "point": [
                    55,
                    56
                ]
            },
            {
                "idx": 101,
                "length": 4,
                "point": [
                    56,
                    57
                ]
            },
            {
                "idx": 102,
                "length": 4,
                "point": [
                    57,
                    58
                ]
            },
            {
                "idx": 103,
                "length": 4,
                "point": [
                    58,
                    59
                ]
            },
            {
                "idx": 104,
                "length": 4,
                "point": [
                    59,
                    60
                ]
            },
            {
                "idx": 105,
                "length": 5,
                "point": [
                    51,
                    61
                ]
            },
            {
                "idx": 106,
                "length": 5,
                "point": [
                    52,
                    62
                ]
            },
            {
                "idx": 107,
                "length": 5,
                "point": [
                    53,
                    63
                ]
            },
            {
                "idx": 108,
                "length": 5,
                "point": [
                    54,
                    64
                ]
            },
            {
                "idx": 109,
                "length": 5,
                "point": [
                    55,
                    65
                ]
            },
            {
                "idx": 110,
                "length": 5,
                "point": [
                    56,
                    66
                ]
            },
            {
                "idx": 111,
                "length": 5,
                "point": [
                    57,
                    67
                ]
            },
            {
                "idx": 112,
                "length": 5,
                "point": [
                    58,
                    68
                ]
            },
            {
                "idx": 113,
                "length": 5,
                "point": [
                    59,
                    69
                ]
            },
            {
                "idx": 114,
                "length": 5,
                "point": [
                    60,
                    70
                ]
            },
            {
                "idx": 115,
                "length": 4,
                "point": [
                    61,
                    62
                ]
            },
            {
                "idx": 116,
                "length": 4,
                "point": [
                    62,
                    63
                ]
            },
            {
                "idx": 117,
                "length": 4,
                "point": [
                    63,
                    64
                ]
            },
            {
                "idx": 118,
                "length": 4,
                "point": [
                    64,
                    65
                ]
            },
            {
                "idx": 119,
                "length": 4,
                "point": [
                    65,
                    66
                ]
            },
            {
                "idx": 120,
                "length": 4,
                "point": [
                    66,
                    67
                ]
            },
            {
                "idx": 121,
                "length": 4,
                "point": [
                    67,
                    68
                ]
            },
            {
                "idx": 122,
                "length": 4,
                "point": [
                    68,
                    69
                ]
            },
            {
                "idx": 123,
                "length": 4,
                "point": [
                    69,
                    70
                ]
            },
            {
                "idx": 124,
                "length": 5,
                "point": [
                    61,
                    71
                ]
            },
            {
                "idx": 125,
                "length": 5,
                "point": [
                    62,
                    72
                ]
            },
            {
                "idx": 126,
                "length": 5,
                "point": [
                    63,
                    73
                ]
            },
            {
                "idx": 127,
                "length": 5,
                "point": [
                    64,
                    74
                ]
            },
            {
                "idx": 128,
                "length": 5,
                "point": [
                    65,
                    75
                ]
            },
            {
                "idx": 129,
                "length": 5,
                "point": [
                    66,
                    76
                ]
            },
            {
                "idx": 130,
                "length": 5,
                "point": [
                    67,
                    77
                ]
            },
            {
                "idx": 131,
                "length": 5,
                "point": [
                    68,
                    78
                ]
            },
            {
                "idx": 132,
                "length": 5,
                "point": [
                    69,
                    79
                ]
            },
            {
                "idx": 133,
                "length": 5,
                "point": [
                    70,
                    80
                ]
            },
            {
                "idx": 134,
                "length": 4,
                "point": [
                    71,
                    72
                ]
            },
            {
                "idx": 135,
                "length": 4,
                "point": [
                    72,
                    73
                ]
            },
            {
                "idx": 136,
                "length": 4,
                "point": [
                    73,
                    74
                ]
            },
            {
                "idx": 137,
                "length": 4,
                "point": [
                    74,
                    75
                ]
            },
            {
                "idx": 138,
                "length": 4,
                "point": [
                    75,
                    76
                ]
            },
            {
                "idx": 139,
                "length": 4,
                "point": [
                    76,
                    77
                ]
            },
            {
                "idx": 140,
                "length": 4,
                "point": [
                    77,
                    78
                ]
            },
            {
                "idx": 141,
                "length": 4,
                "point": [
                    78,
                    79
                ]
            },
            {
                "idx": 142,
                "length": 4,
                "point": [
                    79,
                    80
                ]
            },
            {
                "idx": 143,
                "length": 5,
                "point": [
                    71,
                    81
                ]
            },
            {
                "idx": 144,
                "length": 5,
                "point": [
                    72,
                    82
                ]
            },
            {
                "idx": 145,
                "length": 5,
                "point": [
                    73,
                    83
                ]
            },
            {
                "idx": 146,
                "length": 5,
                "point": [
                    74,
                    84
                ]
            },
            {
                "idx": 147,
                "length": 5,
                "point": [
                    75,
                    85
                ]
            },
            {
                "idx": 148,
                "length": 5,
                "point": [
                    76,
                    86
                ]
            },
            {
                "idx": 149,
                "length": 5,
                "point": [
                    77,
                    87
                ]
            },
            {
                "idx": 150,
                "length": 5,
                "point": [
                    78,
                    88
                ]
            },
            {
                "idx": 151,
                "length": 5,
                "point": [
                    79,
                    89
                ]
            },
            {
                "idx": 152,
                "length": 5,
                "point": [
                    80,
                    90
                ]
            },
            {
                "idx": 153,
                "length": 4,
                "point": [
                    81,
                    82
                ]
            },
            {
                "idx": 154,
                "length": 4,
                "point": [
                    82,
                    83
                ]
            },
            {
                "idx": 155,
                "length": 4,
                "point": [
                    83,
                    84
                ]
            },
            {
                "idx": 156,
                "length": 4,
                "point": [
                    84,
                    85
                ]
            },
            {
                "idx": 157,
                "length": 4,
                "point": [
                    85,
                    86
                ]
            },
            {
                "idx": 158,
                "length": 4,
                "point": [
                    86,
                    87
                ]
            },
            {
                "idx": 159,
                "length": 4,
                "point": [
                    87,
                    88
                ]
            },
            {
                "idx": 160,
                "length": 4,
                "point": [
                    88,
                    89
                ]
            },
            {
                "idx": 161,
                "length": 4,
                "point": [
                    89,
                    90
                ]
            },
            {
                "idx": 162,
                "length": 5,
                "point": [
                    81,
                    91
                ]
            },
            {
                "idx": 163,
                "length": 5,
                "point": [
                    82,
                    92
                ]
            },
            {
                "idx": 164,
                "length": 5,
                "point": [
                    83,
                    93
                ]
            },
            {
                "idx": 165,
                "length": 5,
                "point": [
                    84,
                    94
                ]
            },
            {
                "idx": 166,
                "length": 5,
                "point": [
                    85,
                    95
                ]
            },
            {
                "idx": 167,
                "length": 5,
                "point": [
                    86,
                    96
                ]
            },
            {
                "idx": 168,
                "length": 5,
                "point": [
                    87,
                    97
                ]
            },
            {
                "idx": 169,
                "length": 5,
                "point": [
                    88,
                    98
                ]
            },
            {
                "idx": 170,
                "length": 5,
                "point": [
                    89,
                    99
                ]
            },
            {
                "idx": 171,
                "length": 5,
                "point": [
                    90,
                    100
                ]
            },
            {
                "idx": 172,
                "length": 4,
                "point": [
                    91,
                    92
                ]
            },
            {
                "idx": 173,
                "length": 4,
                "point": [
                    92,
                    93
                ]
            },
            {
                "idx": 174,
                "length": 4,
                "point": [
                    93,
                    94
                ]
            },
            {
                "idx": 175,
                "length": 4,
                "point": [
                    94,
                    95
                ]
            },
            {
                "idx": 176,
                "length": 4,
                "point": [
                    95,
                    96
                ]
            },
            {
                "idx": 177,
                "length": 4,
                "point": [
                    96,
                    97
                ]
            },
            {
                "idx": 178,
                "length": 4,
                "point": [
                    97,
                    98
                ]
            },
            {
                "idx": 179,
                "length": 4,
                "point": [
                    98,
                    99
                ]
            },
            {
                "idx": 180,
                "length": 4,
                "point": [
                    99,
                    100
                ]
            }
        ],
        "name": "theMap",
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
                "post_id": null
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
                "post_id": 4
            },
            {
                "idx": 13,
                "post_id": null
            },
            {
                "idx": 14,
                "post_id": null
            },
            {
                "idx": 15,
                "post_id": null
            },
            {
                "idx": 16,
                "post_id": null
            },
            {
                "idx": 17,
                "post_id": null
            },
            {
                "idx": 18,
                "post_id": null
            },
            {
                "idx": 19,
                "post_id": null
            },
            {
                "idx": 20,
                "post_id": null
            },
            {
                "idx": 21,
                "post_id": null
            },
            {
                "idx": 22,
                "post_id": null
            },
            {
                "idx": 23,
                "post_id": null
            },
            {
                "idx": 24,
                "post_id": null
            },
            {
                "idx": 25,
                "post_id": null
            },
            {
                "idx": 26,
                "post_id": null
            },
            {
                "idx": 27,
                "post_id": null
            },
            {
                "idx": 28,
                "post_id": null
            },
            {
                "idx": 29,
                "post_id": null
            },
            {
                "idx": 30,
                "post_id": null
            },
            {
                "idx": 31,
                "post_id": null
            },
            {
                "idx": 32,
                "post_id": 5
            },
            {
                "idx": 33,
                "post_id": null
            },
            {
                "idx": 34,
                "post_id": null
            },
            {
                "idx": 35,
                "post_id": null
            },
            {
                "idx": 36,
                "post_id": null
            },
            {
                "idx": 37,
                "post_id": null
            },
            {
                "idx": 38,
                "post_id": null
            },
            {
                "idx": 39,
                "post_id": null
            },
            {
                "idx": 40,
                "post_id": null
            },
            {
                "idx": 41,
                "post_id": null
            },
            {
                "idx": 42,
                "post_id": null
            },
            {
                "idx": 43,
                "post_id": null
            },
            {
                "idx": 44,
                "post_id": null
            },
            {
                "idx": 45,
                "post_id": null
            },
            {
                "idx": 46,
                "post_id": null
            },
            {
                "idx": 47,
                "post_id": null
            },
            {
                "idx": 48,
                "post_id": null
            },
            {
                "idx": 49,
                "post_id": 3
            },
            {
                "idx": 50,
                "post_id": null
            },
            {
                "idx": 51,
                "post_id": null
            },
            {
                "idx": 52,
                "post_id": null
            },
            {
                "idx": 53,
                "post_id": null
            },
            {
                "idx": 54,
                "post_id": null
            },
            {
                "idx": 55,
                "post_id": null
            },
            {
                "idx": 56,
                "post_id": 6
            },
            {
                "idx": 57,
                "post_id": null
            },
            {
                "idx": 58,
                "post_id": null
            },
            {
                "idx": 59,
                "post_id": null
            },
            {
                "idx": 60,
                "post_id": null
            },
            {
                "idx": 61,
                "post_id": null
            },
            {
                "idx": 62,
                "post_id": null
            },
            {
                "idx": 63,
                "post_id": null
            },
            {
                "idx": 64,
                "post_id": null
            },
            {
                "idx": 65,
                "post_id": null
            },
            {
                "idx": 66,
                "post_id": null
            },
            {
                "idx": 67,
                "post_id": null
            },
            {
                "idx": 68,
                "post_id": null
            },
            {
                "idx": 69,
                "post_id": null
            },
            {
                "idx": 70,
                "post_id": null
            },
            {
                "idx": 71,
                "post_id": null
            },
            {
                "idx": 72,
                "post_id": null
            },
            {
                "idx": 73,
                "post_id": null
            },
            {
                "idx": 74,
                "post_id": null
            },
            {
                "idx": 75,
                "post_id": null
            },
            {
                "idx": 76,
                "post_id": null
            },
            {
                "idx": 77,
                "post_id": null
            },
            {
                "idx": 78,
                "post_id": null
            },
            {
                "idx": 79,
                "post_id": null
            },
            {
                "idx": 80,
                "post_id": null
            },
            {
                "idx": 81,
                "post_id": null
            },
            {
                "idx": 82,
                "post_id": null
            },
            {
                "idx": 83,
                "post_id": null
            },
            {
                "idx": 84,
                "post_id": null
            },
            {
                "idx": 85,
                "post_id": null
            },
            {
                "idx": 86,
                "post_id": null
            },
            {
                "idx": 87,
                "post_id": null
            },
            {
                "idx": 88,
                "post_id": null
            },
            {
                "idx": 89,
                "post_id": 2
            },
            {
                "idx": 90,
                "post_id": null
            },
            {
                "idx": 91,
                "post_id": null
            },
            {
                "idx": 92,
                "post_id": null
            },
            {
                "idx": 93,
                "post_id": null
            },
            {
                "idx": 94,
                "post_id": null
            },
            {
                "idx": 95,
                "post_id": null
            },
            {
                "idx": 96,
                "post_id": null
            },
            {
                "idx": 97,
                "post_id": null
            },
            {
                "idx": 98,
                "post_id": null
            },
            {
                "idx": 99,
                "post_id": null
            },
            {
                "idx": 100,
                "post_id": null
            }
        ]
    }''')


    map_pos03 = dict([(i+1 , (i//10*1.1/10, (i %10 )*1.1/ 10)) for i in range(0,100)])

    objects03 = json.loads('''{
        "idx": 1,
        "post": [
            {
                "armor": 100,
                "armor_capacity": 100,
                "event": [],
                "idx": 1,
                "level": 1,
                "name": "town-one",
                "next_level_price": 100,
                "player_id": "92b23d2f-81ae-4c2d-b4e5-aa81f70fda8e",
                "point_id": 1,
                "population": 3,
                "population_capacity": 10,
                "product": 350,
                "product_capacity": 200,
                "type": 1
            },
            {
                "event": [],
                "idx": 2,
                "name": "market-big",
                "point_id": 89,
                "product": 500,
                "product_capacity": 500,
                "replenishment": 10,
                "type": 2
            },
            {
                "event": [],
                "idx": 3,
                "name": "market-medium",
                "point_id": 49,
                "product": 250,
                "product_capacity": 250,
                "replenishment": 10,
                "type": 2
            },
            {
                "event": [],
                "idx": 4,
                "name": "market-small",
                "point_id": 12,
                "product": 50,
                "product_capacity": 50,
                "replenishment": 5,
                "type": 2
            },
            {
                "armor": 20,
                "armor_capacity": 20,
                "event": [],
                "idx": 5,
                "name": "storage-small",
                "point_id": 32,
                "replenishment": 1,
                "type": 3
            },
            {
                "armor": 100,
                "armor_capacity": 100,
                "event": [],
                "idx": 6,
                "name": "storage-big",
                "point_id": 56,
                "replenishment": 5,
                "type": 3
            }
        ],
        "train": [
            {
                "event": [],
                "goods": 0,
                "goods_capacity": 40,
                "idx": 1,
                "level": 1,
                "line_idx": 1,
                "next_level_price": 40,
                "player_id": "07f32b23-8127-49f5-ab65-be7d5c775d6a",
                "position": 0,
                "post_type": null,
                "speed": 0
            },
            {
                "event": [],
                "goods": 0,
                "goods_capacity": 40,
                "idx": 2,
                "level": 1,
                "line_idx": 1,
                "next_level_price": 40,
                "player_id": "07f32b23-8127-49f5-ab65-be7d5c775d6a",
                "position": 0,
                "post_type": null,
                "speed": 0
            },
            {
                "event": [],
                "goods": 0,
                "goods_capacity": 40,
                "idx": 3,
                "level": 1,
                "line_idx": 11,
                "next_level_price": 40,
                "player_id": "92b23d2f-81ae-4c2d-b4e5-aa81f70fda8e",
                "position": 3,
                "post_type": null,
                "speed": 0
            }
        ]
    }''')

    map04 = json.loads('''{
        "idx": 1,
        "line": [
        {
            "idx": 1,
            "length": 4,
            "point": [
                1,
                2
            ]
        },
        {
            "idx": 2,
            "length": 4,
            "point": [
                2,
                3
            ]
        },
        {
            "idx": 3,
            "length": 4,
            "point": [
                3,
                4
            ]
        },
        {
            "idx": 4,
            "length": 4,
            "point": [
                4,
                5
            ]
        },
        {
            "idx": 5,
            "length": 4,
            "point": [
                5,
                6
            ]
        },
        {
            "idx": 6,
            "length": 4,
            "point": [
                6,
                7
            ]
        },
        {
            "idx": 7,
            "length": 4,
            "point": [
                7,
                8
            ]
        },
        {
            "idx": 8,
            "length": 4,
            "point": [
                8,
                9
            ]
        },
        {
            "idx": 9,
            "length": 4,
            "point": [
                9,
                10
            ]
        },
        {
            "idx": 10,
            "length": 5,
            "point": [
                1,
                11
            ]
        },
        {
            "idx": 11,
            "length": 5,
            "point": [
                2,
                12
            ]
        },
        {
            "idx": 12,
            "length": 5,
            "point": [
                3,
                13
            ]
        },
        {
            "idx": 13,
            "length": 5,
            "point": [
                4,
                14
            ]
        },
        {
            "idx": 14,
            "length": 5,
            "point": [
                5,
                15
            ]
        },
        {
            "idx": 15,
            "length": 5,
            "point": [
                6,
                16
            ]
        },
        {
            "idx": 16,
            "length": 5,
            "point": [
                7,
                17
            ]
        },
        {
            "idx": 17,
            "length": 5,
            "point": [
                8,
                18
            ]
        },
        {
            "idx": 18,
            "length": 5,
            "point": [
                9,
                19
            ]
        },
        {
            "idx": 19,
            "length": 5,
            "point": [
                10,
                20
            ]
        },
        {
            "idx": 20,
            "length": 4,
            "point": [
                11,
                12
            ]
        },
        {
            "idx": 21,
            "length": 4,
            "point": [
                12,
                13
            ]
        },
        {
            "idx": 22,
            "length": 4,
            "point": [
                13,
                14
            ]
        },
        {
            "idx": 23,
            "length": 4,
            "point": [
                14,
                15
            ]
        },
        {
            "idx": 24,
            "length": 4,
            "point": [
                15,
                16
            ]
        },
        {
            "idx": 25,
            "length": 4,
            "point": [
                16,
                17
            ]
        },
        {
            "idx": 26,
            "length": 4,
            "point": [
                17,
                18
            ]
        },
        {
            "idx": 27,
            "length": 4,
            "point": [
                18,
                19
            ]
        },
        {
            "idx": 28,
            "length": 4,
            "point": [
                19,
                20
            ]
        },
        {
            "idx": 29,
            "length": 5,
            "point": [
                11,
                21
            ]
        },
        {
            "idx": 30,
            "length": 5,
            "point": [
                12,
                22
            ]
        },
        {
            "idx": 31,
            "length": 5,
            "point": [
                13,
                23
            ]
        },
        {
            "idx": 32,
            "length": 5,
            "point": [
                14,
                24
            ]
        },
        {
            "idx": 33,
            "length": 5,
            "point": [
                15,
                25
            ]
        },
        {
            "idx": 34,
            "length": 5,
            "point": [
                16,
                26
            ]
        },
        {
            "idx": 35,
            "length": 5,
            "point": [
                17,
                27
            ]
        },
        {
            "idx": 36,
            "length": 5,
            "point": [
                18,
                28
            ]
        },
        {
            "idx": 37,
            "length": 5,
            "point": [
                19,
                29
            ]
        },
        {
            "idx": 38,
            "length": 5,
            "point": [
                20,
                30
            ]
        },
        {
            "idx": 39,
            "length": 4,
            "point": [
                21,
                22
            ]
        },
        {
            "idx": 40,
            "length": 4,
            "point": [
                22,
                23
            ]
        },
        {
            "idx": 41,
            "length": 4,
            "point": [
                23,
                24
            ]
        },
        {
            "idx": 42,
            "length": 4,
            "point": [
                24,
                25
            ]
        },
        {
            "idx": 43,
            "length": 4,
            "point": [
                25,
                26
            ]
        },
        {
            "idx": 44,
            "length": 4,
            "point": [
                26,
                27
            ]
        },
        {
            "idx": 45,
            "length": 4,
            "point": [
                27,
                28
            ]
        },
        {
            "idx": 46,
            "length": 4,
            "point": [
                28,
                29
            ]
        },
        {
            "idx": 47,
            "length": 4,
            "point": [
                29,
                30
            ]
        },
        {
            "idx": 48,
            "length": 5,
            "point": [
                21,
                31
            ]
        },
        {
            "idx": 49,
            "length": 5,
            "point": [
                22,
                32
            ]
        },
        {
            "idx": 50,
            "length": 5,
            "point": [
                23,
                33
            ]
        },
        {
            "idx": 51,
            "length": 5,
            "point": [
                24,
                34
            ]
        },
        {
            "idx": 52,
            "length": 5,
            "point": [
                25,
                35
            ]
        },
        {
            "idx": 53,
            "length": 5,
            "point": [
                26,
                36
            ]
        },
        {
            "idx": 54,
            "length": 5,
            "point": [
                27,
                37
            ]
        },
        {
            "idx": 55,
            "length": 5,
            "point": [
                28,
                38
            ]
        },
        {
            "idx": 56,
            "length": 5,
            "point": [
                29,
                39
            ]
        },
        {
            "idx": 57,
            "length": 5,
            "point": [
                30,
                40
            ]
        },
        {
            "idx": 58,
            "length": 4,
            "point": [
                31,
                32
            ]
        },
        {
            "idx": 59,
            "length": 4,
            "point": [
                32,
                33
            ]
        },
        {
            "idx": 60,
            "length": 4,
            "point": [
                33,
                34
            ]
        },
        {
            "idx": 61,
            "length": 4,
            "point": [
                34,
                35
            ]
        },
        {
            "idx": 62,
            "length": 4,
            "point": [
                35,
                36
            ]
        },
        {
            "idx": 63,
            "length": 4,
            "point": [
                36,
                37
            ]
        },
        {
            "idx": 64,
            "length": 4,
            "point": [
                37,
                38
            ]
        },
        {
            "idx": 65,
            "length": 4,
            "point": [
                38,
                39
            ]
        },
        {
            "idx": 66,
            "length": 4,
            "point": [
                39,
                40
            ]
        },
        {
            "idx": 67,
            "length": 5,
            "point": [
                31,
                41
            ]
        },
        {
            "idx": 68,
            "length": 5,
            "point": [
                32,
                42
            ]
        },
        {
            "idx": 69,
            "length": 5,
            "point": [
                33,
                43
            ]
        },
        {
            "idx": 70,
            "length": 5,
            "point": [
                34,
                44
            ]
        },
        {
            "idx": 71,
            "length": 5,
            "point": [
                35,
                45
            ]
        },
        {
            "idx": 72,
            "length": 5,
            "point": [
                36,
                46
            ]
        },
        {
            "idx": 73,
            "length": 5,
            "point": [
                37,
                47
            ]
        },
        {
            "idx": 74,
            "length": 5,
            "point": [
                38,
                48
            ]
        },
        {
            "idx": 75,
            "length": 5,
            "point": [
                39,
                49
            ]
        },
        {
            "idx": 76,
            "length": 5,
            "point": [
                40,
                50
            ]
        },
        {
            "idx": 77,
            "length": 4,
            "point": [
                41,
                42
            ]
        },
        {
            "idx": 78,
            "length": 4,
            "point": [
                42,
                43
            ]
        },
        {
            "idx": 79,
            "length": 4,
            "point": [
                43,
                44
            ]
        },
        {
            "idx": 80,
            "length": 4,
            "point": [
                44,
                45
            ]
        },
        {
            "idx": 81,
            "length": 2,
            "point": [
                45,
                46
            ]
        },
        {
            "idx": 82,
            "length": 4,
            "point": [
                46,
                47
            ]
        },
        {
            "idx": 83,
            "length": 4,
            "point": [
                47,
                48
            ]
        },
        {
            "idx": 84,
            "length": 4,
            "point": [
                48,
                49
            ]
        },
        {
            "idx": 85,
            "length": 4,
            "point": [
                49,
                50
            ]
        },
        {
            "idx": 86,
            "length": 5,
            "point": [
                41,
                51
            ]
        },
        {
            "idx": 87,
            "length": 5,
            "point": [
                42,
                52
            ]
        },
        {
            "idx": 88,
            "length": 5,
            "point": [
                43,
                53
            ]
        },
        {
            "idx": 89,
            "length": 5,
            "point": [
                44,
                54
            ]
        },
        {
            "idx": 90,
            "length": 2,
            "point": [
                45,
                55
            ]
        },
        {
            "idx": 91,
            "length": 2,
            "point": [
                46,
                56
            ]
        },
        {
            "idx": 92,
            "length": 5,
            "point": [
                47,
                57
            ]
        },
        {
            "idx": 93,
            "length": 5,
            "point": [
                48,
                58
            ]
        },
        {
            "idx": 94,
            "length": 5,
            "point": [
                49,
                59
            ]
        },
        {
            "idx": 95,
            "length": 5,
            "point": [
                50,
                60
            ]
        },
        {
            "idx": 96,
            "length": 4,
            "point": [
                51,
                52
            ]
        },
        {
            "idx": 97,
            "length": 4,
            "point": [
                52,
                53
            ]
        },
        {
            "idx": 98,
            "length": 4,
            "point": [
                53,
                54
            ]
        },
        {
            "idx": 99,
            "length": 4,
            "point": [
                54,
                55
            ]
        },
        {
            "idx": 100,
            "length": 2,
            "point": [
                55,
                56
            ]
        },
        {
            "idx": 101,
            "length": 4,
            "point": [
                56,
                57
            ]
        },
        {
            "idx": 102,
            "length": 4,
            "point": [
                57,
                58
            ]
        },
        {
            "idx": 103,
            "length": 4,
            "point": [
                58,
                59
            ]
        },
        {
            "idx": 104,
            "length": 4,
            "point": [
                59,
                60
            ]
        },
        {
            "idx": 105,
            "length": 5,
            "point": [
                51,
                61
            ]
        },
        {
            "idx": 106,
            "length": 5,
            "point": [
                52,
                62
            ]
        },
        {
            "idx": 107,
            "length": 5,
            "point": [
                53,
                63
            ]
        },
        {
            "idx": 108,
            "length": 5,
            "point": [
                54,
                64
            ]
        },
        {
            "idx": 109,
            "length": 5,
            "point": [
                55,
                65
            ]
        },
        {
            "idx": 110,
            "length": 5,
            "point": [
                56,
                66
            ]
        },
        {
            "idx": 111,
            "length": 5,
            "point": [
                57,
                67
            ]
        },
        {
            "idx": 112,
            "length": 5,
            "point": [
                58,
                68
            ]
        },
        {
            "idx": 113,
            "length": 5,
            "point": [
                59,
                69
            ]
        },
        {
            "idx": 114,
            "length": 5,
            "point": [
                60,
                70
            ]
        },
        {
            "idx": 115,
            "length": 4,
            "point": [
                61,
                62
            ]
        },
        {
            "idx": 116,
            "length": 4,
            "point": [
                62,
                63
            ]
        },
        {
            "idx": 117,
            "length": 4,
            "point": [
                63,
                64
            ]
        },
        {
            "idx": 118,
            "length": 4,
            "point": [
                64,
                65
            ]
        },
        {
            "idx": 119,
            "length": 4,
            "point": [
                65,
                66
            ]
        },
        {
            "idx": 120,
            "length": 4,
            "point": [
                66,
                67
            ]
        },
        {
            "idx": 121,
            "length": 4,
            "point": [
                67,
                68
            ]
        },
        {
            "idx": 122,
            "length": 4,
            "point": [
                68,
                69
            ]
        },
        {
            "idx": 123,
            "length": 4,
            "point": [
                69,
                70
            ]
        },
        {
            "idx": 124,
            "length": 5,
            "point": [
                61,
                71
            ]
        },
        {
            "idx": 125,
            "length": 5,
            "point": [
                62,
                72
            ]
        },
        {
            "idx": 126,
            "length": 5,
            "point": [
                63,
                73
            ]
        },
        {
            "idx": 127,
            "length": 5,
            "point": [
                64,
                74
            ]
        },
        {
            "idx": 128,
            "length": 5,
            "point": [
                65,
                75
            ]
        },
        {
            "idx": 129,
            "length": 5,
            "point": [
                66,
                76
            ]
        },
        {
            "idx": 130,
            "length": 5,
            "point": [
                67,
                77
            ]
        },
        {
            "idx": 131,
            "length": 5,
            "point": [
                68,
                78
            ]
        },
        {
            "idx": 132,
            "length": 5,
            "point": [
                69,
                79
            ]
        },
        {
            "idx": 133,
            "length": 5,
            "point": [
                70,
                80
            ]
        },
        {
            "idx": 134,
            "length": 4,
            "point": [
                71,
                72
            ]
        },
        {
            "idx": 135,
            "length": 4,
            "point": [
                72,
                73
            ]
        },
        {
            "idx": 136,
            "length": 4,
            "point": [
                73,
                74
            ]
        },
        {
            "idx": 137,
            "length": 4,
            "point": [
                74,
                75
            ]
        },
        {
            "idx": 138,
            "length": 4,
            "point": [
                75,
                76
            ]
        },
        {
            "idx": 139,
            "length": 4,
            "point": [
                76,
                77
            ]
        },
        {
            "idx": 140,
            "length": 4,
            "point": [
                77,
                78
            ]
        },
        {
            "idx": 141,
            "length": 4,
            "point": [
                78,
                79
            ]
        },
        {
            "idx": 142,
            "length": 4,
            "point": [
                79,
                80
            ]
        },
        {
            "idx": 143,
            "length": 5,
            "point": [
                71,
                81
            ]
        },
        {
            "idx": 144,
            "length": 5,
            "point": [
                72,
                82
            ]
        },
        {
            "idx": 145,
            "length": 5,
            "point": [
                73,
                83
            ]
        },
        {
            "idx": 146,
            "length": 5,
            "point": [
                74,
                84
            ]
        },
        {
            "idx": 147,
            "length": 5,
            "point": [
                75,
                85
            ]
        },
        {
            "idx": 148,
            "length": 5,
            "point": [
                76,
                86
            ]
        },
        {
            "idx": 149,
            "length": 5,
            "point": [
                77,
                87
            ]
        },
        {
            "idx": 150,
            "length": 5,
            "point": [
                78,
                88
            ]
        },
        {
            "idx": 151,
            "length": 5,
            "point": [
                79,
                89
            ]
        },
        {
            "idx": 152,
            "length": 5,
            "point": [
                80,
                90
            ]
        },
        {
            "idx": 153,
            "length": 4,
            "point": [
                81,
                82
            ]
        },
        {
            "idx": 154,
            "length": 4,
            "point": [
                82,
                83
            ]
        },
        {
            "idx": 155,
            "length": 4,
            "point": [
                83,
                84
            ]
        },
        {
            "idx": 156,
            "length": 4,
            "point": [
                84,
                85
            ]
        },
        {
            "idx": 157,
            "length": 4,
            "point": [
                85,
                86
            ]
        },
        {
            "idx": 158,
            "length": 4,
            "point": [
                86,
                87
            ]
        },
        {
            "idx": 159,
            "length": 4,
            "point": [
                87,
                88
            ]
        },
        {
            "idx": 160,
            "length": 4,
            "point": [
                88,
                89
            ]
        },
        {
            "idx": 161,
            "length": 4,
            "point": [
                89,
                90
            ]
        },
        {
            "idx": 162,
            "length": 5,
            "point": [
                81,
                91
            ]
        },
        {
            "idx": 163,
            "length": 5,
            "point": [
                82,
                92
            ]
        },
        {
            "idx": 164,
            "length": 5,
            "point": [
                83,
                93
            ]
        },
        {
            "idx": 165,
            "length": 5,
            "point": [
                84,
                94
            ]
        },
        {
            "idx": 166,
            "length": 5,
            "point": [
                85,
                95
            ]
        },
        {
            "idx": 167,
            "length": 5,
            "point": [
                86,
                96
            ]
        },
        {
            "idx": 168,
            "length": 5,
            "point": [
                87,
                97
            ]
        },
        {
            "idx": 169,
            "length": 5,
            "point": [
                88,
                98
            ]
        },
        {
            "idx": 170,
            "length": 5,
            "point": [
                89,
                99
            ]
        },
        {
            "idx": 171,
            "length": 5,
            "point": [
                90,
                100
            ]
        },
        {
            "idx": 172,
            "length": 4,
            "point": [
                91,
                92
            ]
        },
        {
            "idx": 173,
            "length": 4,
            "point": [
                92,
                93
            ]
        },
        {
            "idx": 174,
            "length": 4,
            "point": [
                93,
                94
            ]
        },
        {
            "idx": 175,
            "length": 4,
            "point": [
                94,
                95
            ]
        },
        {
            "idx": 176,
            "length": 4,
            "point": [
                95,
                96
            ]
        },
        {
            "idx": 177,
            "length": 4,
            "point": [
                96,
                97
            ]
        },
        {
            "idx": 178,
            "length": 4,
            "point": [
                97,
                98
            ]
        },
        {
            "idx": 179,
            "length": 4,
            "point": [
                98,
                99
            ]
        },
        {
            "idx": 180,
            "length": 4,
            "point": [
                99,
                100
            ]
        }
        ],
        "name": "theMap",
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
            "post_id": null
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
            "post_id": 2
        },
        {
            "idx": 11,
            "post_id": null
        },
        {
            "idx": 12,
            "post_id": null
        },
        {
            "idx": 13,
            "post_id": null
        },
        {
            "idx": 14,
            "post_id": null
        },
        {
            "idx": 15,
            "post_id": null
        },
        {
            "idx": 16,
            "post_id": null
        },
        {
            "idx": 17,
            "post_id": null
        },
        {
            "idx": 18,
            "post_id": null
        },
        {
            "idx": 19,
            "post_id": null
        },
        {
            "idx": 20,
            "post_id": null
        },
        {
            "idx": 21,
            "post_id": null
        },
        {
            "idx": 22,
            "post_id": null
        },
        {
            "idx": 23,
            "post_id": null
        },
        {
            "idx": 24,
            "post_id": null
        },
        {
            "idx": 25,
            "post_id": null
        },
        {
            "idx": 26,
            "post_id": null
        },
        {
            "idx": 27,
            "post_id": null
        },
        {
            "idx": 28,
            "post_id": null
        },
        {
            "idx": 29,
            "post_id": null
        },
        {
            "idx": 30,
            "post_id": null
        },
        {
            "idx": 31,
            "post_id": null
        },
        {
            "idx": 32,
            "post_id": null
        },
        {
            "idx": 33,
            "post_id": null
        },
        {
            "idx": 34,
            "post_id": 5
        },
        {
            "idx": 35,
            "post_id": null
        },
        {
            "idx": 36,
            "post_id": null
        },
        {
            "idx": 37,
            "post_id": 6
        },
        {
            "idx": 38,
            "post_id": null
        },
        {
            "idx": 39,
            "post_id": null
        },
        {
            "idx": 40,
            "post_id": null
        },
        {
            "idx": 41,
            "post_id": null
        },
        {
            "idx": 42,
            "post_id": null
        },
        {
            "idx": 43,
            "post_id": null
        },
        {
            "idx": 44,
            "post_id": null
        },
        {
            "idx": 45,
            "post_id": 9
        },
        {
            "idx": 46,
            "post_id": 10
        },
        {
            "idx": 47,
            "post_id": null
        },
        {
            "idx": 48,
            "post_id": null
        },
        {
            "idx": 49,
            "post_id": null
        },
        {
            "idx": 50,
            "post_id": null
        },
        {
            "idx": 51,
            "post_id": null
        },
        {
            "idx": 52,
            "post_id": null
        },
        {
            "idx": 53,
            "post_id": null
        },
        {
            "idx": 54,
            "post_id": null
        },
        {
            "idx": 55,
            "post_id": 11
        },
        {
            "idx": 56,
            "post_id": 12
        },
        {
            "idx": 57,
            "post_id": null
        },
        {
            "idx": 58,
            "post_id": null
        },
        {
            "idx": 59,
            "post_id": null
        },
        {
            "idx": 60,
            "post_id": null
        },
        {
            "idx": 61,
            "post_id": null
        },
        {
            "idx": 62,
            "post_id": null
        },
        {
            "idx": 63,
            "post_id": null
        },
        {
            "idx": 64,
            "post_id": 7
        },
        {
            "idx": 65,
            "post_id": null
        },
        {
            "idx": 66,
            "post_id": null
        },
        {
            "idx": 67,
            "post_id": 8
        },
        {
            "idx": 68,
            "post_id": null
        },
        {
            "idx": 69,
            "post_id": null
        },
        {
            "idx": 70,
            "post_id": null
        },
        {
            "idx": 71,
            "post_id": null
        },
        {
            "idx": 72,
            "post_id": null
        },
        {
            "idx": 73,
            "post_id": null
        },
        {
            "idx": 74,
            "post_id": null
        },
        {
            "idx": 75,
            "post_id": null
        },
        {
            "idx": 76,
            "post_id": null
        },
        {
            "idx": 77,
            "post_id": null
        },
        {
            "idx": 78,
            "post_id": null
        },
        {
            "idx": 79,
            "post_id": null
        },
        {
            "idx": 80,
            "post_id": null
        },
        {
            "idx": 81,
            "post_id": null
        },
        {
            "idx": 82,
            "post_id": null
        },
        {
            "idx": 83,
            "post_id": null
        },
        {
            "idx": 84,
            "post_id": null
        },
        {
            "idx": 85,
            "post_id": null
        },
        {
            "idx": 86,
            "post_id": null
        },
        {
            "idx": 87,
            "post_id": null
        },
        {
            "idx": 88,
            "post_id": null
        },
        {
            "idx": 89,
            "post_id": null
        },
        {
            "idx": 90,
            "post_id": null
        },
        {
            "idx": 91,
            "post_id": 3
        },
        {
            "idx": 92,
            "post_id": null
        },
        {
            "idx": 93,
            "post_id": null
        },
        {
            "idx": 94,
            "post_id": null
        },
        {
            "idx": 95,
            "post_id": null
        },
        {
            "idx": 96,
            "post_id": null
        },
        {
            "idx": 97,
            "post_id": null
        },
        {
            "idx": 98,
            "post_id": null
        },
        {
            "idx": 99,
            "post_id": null
        },
        {
            "idx": 100,
            "post_id": 4
        }
        ]
    }''')

    objects04 = json.loads('''{
        "idx": 1,
        "post": [
        {
            "armor": 100,
            "armor_capacity": 200,
            "event": [],
            "idx": 1,
            "level": 1,
            "name": "Kiev",
            "next_level_price": 100,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "point_id": 1,
            "population": 3,
            "population_capacity": 10,
            "product": 200,
            "product_capacity": 200,
            "train_cooldown_on_collision": 2,
            "type": 1
        },
        {
            "armor": 100,
            "armor_capacity": 200,
            "event": [],
            "idx": 2,
            "level": 1,
            "name": "Minsk",
            "next_level_price": 100,
            "player_id": null,
            "point_id": 10,
            "population": 3,
            "population_capacity": 10,
            "product": 200,
            "product_capacity": 200,
            "train_cooldown_on_collision": 2,
            "type": 1
        },
        {
            "armor": 100,
            "armor_capacity": 200,
            "event": [],
            "idx": 3,
            "level": 1,
            "name": "Saint Petersburg",
            "next_level_price": 100,
            "player_id": null,
            "point_id": 91,
            "population": 3,
            "population_capacity": 10,
            "product": 200,
            "product_capacity": 200,
            "train_cooldown_on_collision": 2,
            "type": 1
        },
        {
            "armor": 100,
            "armor_capacity": 200,
            "event": [],
            "idx": 4,
            "level": 1,
            "name": "Tallinn",
            "next_level_price": 100,
            "player_id": null,
            "point_id": 100,
            "population": 3,
            "population_capacity": 10,
            "product": 200,
            "product_capacity": 200,
            "train_cooldown_on_collision": 2,
            "type": 1
        },
        {
            "event": [],
            "idx": 5,
            "name": "market-01",
            "point_id": 34,
            "product": 500,
            "product_capacity": 500,
            "replenishment": 10,
            "type": 2
        },
        {
            "event": [],
            "idx": 6,
            "name": "market-02",
            "point_id": 37,
            "product": 500,
            "product_capacity": 500,
            "replenishment": 10,
            "type": 2
        },
        {
            "event": [],
            "idx": 7,
            "name": "market-03",
            "point_id": 64,
            "product": 500,
            "product_capacity": 500,
            "replenishment": 10,
            "type": 2
        },
        {
            "event": [],
            "idx": 8,
            "name": "market-04",
            "point_id": 67,
            "product": 500,
            "product_capacity": 500,
            "replenishment": 10,
            "type": 2
        },
        {
            "armor": 100,
            "armor_capacity": 100,
            "event": [],
            "idx": 9,
            "name": "storage-01",
            "point_id": 45,
            "replenishment": 15,
            "type": 3
        },
        {
            "armor": 100,
            "armor_capacity": 100,
            "event": [],
            "idx": 10,
            "name": "storage-02",
            "point_id": 46,
            "replenishment": 15,
            "type": 3
        },
        {
            "armor": 100,
            "armor_capacity": 100,
            "event": [],
            "idx": 11,
            "name": "storage-03",
            "point_id": 55,
            "replenishment": 15,
            "type": 3
        },
        {
            "armor": 100,
            "armor_capacity": 100,
            "event": [],
            "idx": 12,
            "name": "storage-04",
            "point_id": 56,
            "replenishment": 15,
            "type": 3
        }
        ],
        "rating": {
            "Mickey": 3300
        },
        "train": [
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 1,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 2,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 3,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 4,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 5,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 6,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 7,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
            "speed": 0
        },
        {
            "cooldown": 0,
            "event": [],
            "goods": 0,
            "goods_capacity": 40,
            "idx": 8,
            "level": 1,
            "line_idx": 1,
            "next_level_price": 40,
            "player_id": "0d3b36f0-0a4e-479a-a8fa-0e0d1fc9cb9e",
            "position": 0,
            "post_type": null,
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

    def get_pos(self):
        return getattr(self, "map_pos%02d" % self.num)
