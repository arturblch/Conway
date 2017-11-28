import json
from model.Map import Map


map01 = Map(json.loads('''{
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

map02 = Map(json.loads('''{
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
}'''))