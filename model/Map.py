import networkx as nx


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from([(point.pop('idx'), point)
                                   for point in response["point"]])
        self.Graph.add_edges_from([
            line['point'] + [
                {
                    'length': line['length']
                },
            ] for line in response["line"]
        ])

        self.line = {line.pop('idx'): line for line in response["line"]}

        self.pos = nx.spring_layout(self.Graph, weight="length")

    def get_first_neighbor(self, point):
        neighbors = list(self.Graph.neighbors(point))
        return neighbors[0]
