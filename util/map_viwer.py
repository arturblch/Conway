import networkx as nx
import matplotlib.pyplot as plt
import math
from util.maps import map02
from model.Objects import Objects

import json
G = nx.Graph()

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

line = _map.lines[train_obj.line_idx]

(x1, y1) = _map.pos[line.start_point]
(x2, y2) = _map.pos[line.end_point]
train_pos = train_obj.position / line.length
(x, y) = (x2 * train_pos + x1 * (1.0 - train_pos),
          y2 * train_pos + y1 * (1.0 - train_pos))

if train_obj.speed == -1:
    angle = math.atan2(y2 - y1, x2 - x1) / (
        2.0 * math.pi) * 360  # degrees
elif train_obj.speed == 1:
    angle = math.atan2(y1 - y2, x1 - x2) / (
        2.0 * math.pi) * 360  # degrees
else:
    angle = None



print('angel = ', angle)


print(x, y)
plt.show()
