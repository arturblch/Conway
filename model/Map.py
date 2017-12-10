import networkx as nx
from model.Line import Line
from model.Point import Point


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.lines = {line['idx']: Line(**line) for line in response["line"]}
        self.points = [point['idx'] for point in response["point"]]
        self.posts = [point['post_id'] for point in response["point"] if point['post_id'] is not None]
        self.Graph.add_nodes_from(self.points)
        self.Graph.add_edges_from([(*line['point'], {
            'length': line['length'], 'line': Line(**line)
        }) for line in response["line"]])
        self.pos = nx.spring_layout(
            self.Graph, scale=0.5, center=(0.5, 0.5), iterations=200, weight="length")

    def get_neighbors(self, point):
        return list(self.Graph.neighbors(point))

    # def define_points(self, objects):
    #     posts = list(objects.towns.values()) + list(objects.markets.values()) + list(objects.storages.values())
    #     for post in posts:
    #         post.point = self.points[post.point_id]

    def departure(self, train, arrival_point):                        # можно преоразовать сразу в Move
        if train.point:
            departure_point = train.point
            line = self.Graph.get_edge_data(departure_point, arrival_point)['line']
        else:
            line = train.line_idx
        speed = 1 if line.end_point == arrival_point else -1
        return line, speed

    def get_distance(self, u, v):
        return nx.shortest_path_length(self.Graph, source=u, target=v, weight='length')

    def get_next_point(self, u, v):
        next_point = nx.shortest_path(self.Graph, source=u, target=v)[1]
        return next_point

    def get_train_point(self, train):
        current_line = self.lines[train.line_idx]
        if train.position == current_line.length:
            return current_line.end_point
        elif train.position == 0:
            return current_line.start_point
        return None
