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
        self.post_id = {
            point['post_id']: point['idx']
            for point in response["point"] if point['post_id'] != None
        }
        self.Graph.add_nodes_from(self.points.keys())
        self.Graph.add_edges_from([(*line['point'], {
            'length': line['length'], 'line': Line(**line)
        }) for line in response["line"]])
        self.pos = nx.spring_layout(
            self.Graph, scale=0.5, center=(0.5, 0.5), iterations=200, weight="length")

    def get_neighbors(self, point):
        return list(self.Graph.neighbors(point))

    def define_points(self, objects):
        posts = list(objects.towns.values()) + list(objects.markets.values()) + list(objects.storages.values())
        for post in posts:
            post.point = self.points[post.point_id]

    # TODO:
    # 1. delete departure_point (departure_point == train.point)
    # 2. add departure from any position of the line
    def departure(self, departure_point, arrival_point):                        # можно преоразовать сразу в Move
        line = self.Graph.get_edge_data(departure_point, arrival_point)['line']
        speed = 1 if line.start_point == departure_point else -1
        return line, speed

    def get_distance(self, u, v):
        return nx.shortest_path_length(self.Graph, source=u, target=v, weight='length')

    def get_next_point(self, u, v):
        next_point_idx = nx.shortest_path(self.Graph, source=u, target=v)[1]
        return self.points[next_point_idx]

    def get_train_point(self, train):
        current_line = self.lines[train.line_idx]
        if train.position == current_line.length:
            return self.points[current_line.end_point]
        elif train.position == 0:
            return self.points[current_line.start_point]
        return None
