import networkx as nx


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from([(point.pop('idx'),point) for point in response["point"]])
        self.Graph.add_edges_from([line.pop('point')+[line,] for line in response["line"]])

        self.pos = nx.spectral_layout(self.Graph, weight="length", scale=1, center=(0.5, 0.5))

    def get_first_neighbor(self, point):
        neighbors = list(self.Graph.neighbors(point))
        return neighbors[0]

    def get_line(self, u, v):
        return self.Graph.get_edge_data(u, v)['idx']

    def find_line(self, key, value):
        for e in self.Graph.edges(data=True):
            if e[2]['idx']==value:
                return e
