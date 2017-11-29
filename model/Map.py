import networkx as nx
from model.Line import Line


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from([(point.pop('idx'), point)
                                   for point in response["point"]])
        self.Graph.add_edges_from([
            line['point'] + [
                {
                    'length': line['length'],
                    'idx': line['idx']
                },
            ] for line in response["line"]
        ])

        self.lines = {line.pop('idx'): Line(**line) for line in response["line"]}

        self.pos = nx.spring_layout(self.Graph, weight="length")

    def get_first_neighbor(self, point):
        neighbors = list(self.Graph.neighbors(point))
        return neighbors[0]

    def get_point(self, line_idx, position):
        line = self.lines[line_idx]
        if position == 0:
            return line.start_point
        elif position == line.length:
            return line.end_point

    def departure(self, departure_point, arrival_point):
        line_idx = self.Graph.get_edge_data(departure_point, arrival_point)['idx']
        speed = 1 if self.lines[line_idx].start_point == departure_point else -1
        return line_idx, speed
