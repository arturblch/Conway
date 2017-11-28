import networkx as nx


class Map:
    def __init__(self, responce):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from([(point.pop('idx'), point)
                                   for point in responce["point"]])
        self.Graph.add_edges_from([
            line['point'] + [
                {
                    'length': line['length']
                },
            ] for line in responce["line"]
        ])

        self.line = {line.pop('idx'): line for line in responce["line"]}

        self.pos = nx.spectral_layout(self.Graph, weight="length")

    def get_first_neighbor(self, point):
        neighbors = list(self.Graph.neighbors(point))
        return neighbors[0]
