import networkx as nx
import matplotlib.pyplot as plt

import json
G = nx.Graph()


class Map:
    def __init__(self, responce):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from([(point.pop('idx'), point)
                                   for point in responce["point"]])
        self.Graph.add_edges_from(
            [line.pop('point') + [
                line,
            ] for line in responce["line"]])

        self.pos = nx.spectral_layout(self.Graph, weight="length")


class Objects:
    def __init__(self, response):
        self.trains = {train['idx']: train for train in response['train']}
        self.posts = {post['idx']: post for post in response['post']}

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
            "speed": 0
        }
    ]
}'''))

_map = Map(json.loads('''{
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




nx.draw_networkx_nodes(_map.Graph, _map.pos, node_color='k')
nx.draw_networkx_labels(_map.Graph, _map.pos, font_color='w')
nx.draw_networkx_edges(_map.Graph, _map.pos, width=1.0, edge_color="k")

train_obj = objects.trains[0]
line = _map.Graph.edges(train_obj['line_idx'])[0]

print(line)

(x1, y1) = _map.pos[line[0]]
(x2, y2) = _map.pos[line[1]]
train_pos = train_obj['position']/line['length']
(x, y) = (x1 * train_pos + x2 * (1.0 - train_pos),
y1 * train_pos + y2 * (1.0 - train_pos))

plt.show()
