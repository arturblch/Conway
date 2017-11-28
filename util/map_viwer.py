import networkx as nx
import matplotlib.pyplot as plt
import math
from util.maps import map02

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

        self.pos = nx.spectral_layout(self.Graph, weight="length", scale=1, center=(0.5, 0.5))


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
            "speed": 1
        }
    ]
}'''))

_map = map02

nx.draw_networkx_nodes(_map.Graph, _map.pos, node_color='k')
nx.draw_networkx_labels(_map.Graph, _map.pos, font_color='w')
nx.draw_networkx_edges(_map.Graph, _map.pos, width=1.0, edge_color="k")

train_obj = objects.trains[0]

def finde_line(G, key, value):
    for a in G.edges(data=True):
        print(a)
        if a[2][key]==value:
            return a

line = list(_map.Graph.edges(data=True))[0]


print(line)

(x1, y1) = _map.pos[line[0]]
(x2, y2) = _map.pos[line[1]]
train_pos = train_obj['position']/line[2]['length']


(x, y) = (x2 * train_pos + x1 * (1.0 - train_pos),
y2 * train_pos + y1 * (1.0 - train_pos))

if train_obj['speed'] == 1:
    angle = math.atan2(y2-y1, x2-x1)/(2.0*math.pi)*360  # degrees
elif train_obj['speed'] == -1:
    angle = math.atan2(y1-y2, x1-x2)/(2.0*math.pi)*360  # degrees
else:
    angle = None



print('angel = ', angle)


print(x, y)
plt.show()
