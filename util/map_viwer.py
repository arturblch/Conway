import networkx as nx
import matplotlib.pyplot as plt
import math
from util.WorldGetter import WorldGetter
from model.Map import Map

import json
G = nx.Graph()

factory = WorldGetter(3)
_map = Map(factory.get_map())
_map.pos = dict([(i+1 , (i//10/10, (i %10 )/ 10)) for i in range(0,100)])

print(_map.pos)

nx.draw_networkx_nodes(_map.Graph, _map.pos, node_color='k')
nx.draw_networkx_labels(_map.Graph, _map.pos, font_color='w')
nx.draw_networkx_edges(_map.Graph, _map.pos, width=1.0, edge_color="k")

plt.show()
