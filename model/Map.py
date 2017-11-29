import networkx as nx
from model.Line import Line
from model.Point import Point


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.lines = {line['idx']: Line(**line) for line in response["line"]}
        self.Graph.add_nodes_from([Point(**point) for point in response["point"]])
        self.Graph.add_edges_from([
            (*line['point'], {'length': line['length'], 'line': Line(**line)})
            for line in response["line"]])
        self.pos = nx.spring_layout(self.Graph, weight="length")

    def get_neighbors(self, point):
        return list(self.Graph.neighbors(point))

    def get_point(self, line_idx, position):
        line = self.lines[line_idx]
        if position == 0:
            return line.start_point
        elif position == line.length:
            return line.end_point

    def departure(self, departure_point, arrival_point):
        line = self.Graph.get_edge_data(departure_point, arrival_point)['line']
        speed = 1 if line.start_point == departure_point else -1
        return line, speed
