import networkx as nx
from model.Line import Line
from model.Point import Point


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.lines = {line['idx']: Line(**line) for line in response["line"]}
        self.points = {
            point['idx']: Point(**point)
            for point in response["point"]
        }
        self.Graph.add_nodes_from(self.points.keys())
        self.Graph.add_edges_from([(*line['point'], {
            'length': line['length'], 'line': Line(**line)
        }) for line in response["line"]])
        self.pos = nx.spring_layout(
            self.Graph, scale=0.5, center=(0.5, 0.5), iterations=200, weight="length")

    def get_neighbors(self, point):
        return list(self.Graph.neighbors(point))

    def get_point(self, line_idx, position):  # нужно перенести в Train.node при Update хз как
        line = self.lines[line_idx]
        if position == 0:
            return self.points[line.start_point]
        elif position == line.length:
            return self.points[line.end_point]
        else:
            return None

    def departure(self, departure_point, arrival_point):                        # можно преоразовать сразу в Move
        line = self.Graph.get_edge_data(departure_point, arrival_point)['line']
        speed = 1 if line.start_point == departure_point else -1
        return line, speed

    def get_distance(self, u, v):
        return nx.shortest_path_length(self.Graph, source=u, target=v, weight='length')

    def get_next_point(self, u, v):
        next_point_idx = nx.shortest_path(self.Graph, source=u, target=v)[1]
        return self.points[next_point_idx]

    def get_market_point(self, market):                      # убрать новая фича в объекте
        for point in self.points.values():
            if point.post_id == market.idx:
                return point

    def get_post(self, idx):                                  # может создать отдельный дикт??
        for point in self.points.values():
            if point.idx == idx:
                return point
