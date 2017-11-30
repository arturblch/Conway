import pytest
from model.Map import Map
import json

map_resp = json.loads('''{
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


def test_init():
    test_map = Map(map_resp)

    assert list(
        test_map.Graph.nodes) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    assert test_map.lines[3].length == 10
    assert test_map.lines[3].start_point  == 9
    assert test_map.lines[3].end_point  == 3

