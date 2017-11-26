import networkx as nx


class Map:
    def __init__(self, responce):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from([(point.pop('idx'),point) for point in responce["point"]])
        self.Graph.add_edges_from([line.pop('point')+[line,] for line in responce["line"]])

        self.pos = nx.spectral_layout(self.Graph, weight="length")

    def get_first_neighbor(self, point):
        neighbors = list(self.Graph.neighbors(point))
        return neighbors[0]

    def get_line(self, u, v):
        return self.Graph.get_edge_data(u, v)['idx']
