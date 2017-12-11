import networkx as nx
from model.Line import Line
from model.Point import Point


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.lines = {line['idx']: Line(**line) for line in response["line"]}
        self.points = [point['idx'] for point in response["point"]]
        self.posts = {point['idx']: point['post_id'] for point in response["point"] if point['post_id'] is not None}
        self.Graph.add_nodes_from(self.points)
        self.Graph.add_edges_from([(*line['point'], {
            'length': line['length'], 'line': Line(**line)
        }) for line in response["line"]])
        self.pos = nx.spring_layout(
            self.Graph, scale=0.5, center=(0.5, 0.5), iterations=200, weight="length")
        self.markets = None
        self.storages = None

    def define_posts(self, objects):
        self.markets = [market.point for market in objects.markets.values()]
        self.storages = [storage.point for storage in objects.storages.values()]

    def get_neighbors(self, point):
        return list(self.Graph.neighbors(point))

    def departure(self, train, arrival_point, busy_lines, busy_points):       # можно преоразовать сразу в Move
        if arrival_point in self.markets:
            pr_type = 2
        elif arrival_point in self.storages:
            pr_type = 3
        else:
            pr_type = 1
        if train.point:
            departure_point = train.point
            next_point = self.get_next_point(departure_point, arrival_point, busy_lines, busy_points, pr_type)
            line = self.Graph.get_edge_data(departure_point, next_point)['line']
        else:
            next_point = arrival_point
            line = train.line_idx
        speed = 1 if line.end_point == next_point else -1
        return line, speed, next_point

    def get_distance(self, u, v):
        return nx.shortest_path_length(self.Graph, source=u, target=v, weight='length')

    def get_next_point(self, u, v, busy_lines, busy_points, pr_type):
        for path in nx.shortest_simple_paths(self.Graph, source=u, target=v):
            next_point = path[1]
            line = self.Graph.get_edge_data(u, next_point)['line'].idx
            if line not in busy_lines and next_point not in busy_points:
                if (pr_type == 2 and next_point not in self.storages) or (pr_type == 3 and next_point not in self.markets) or pr_type == 1:
                    return next_point

    def get_train_point(self, train):
        current_line = self.lines[train.line_idx]
        if train.position == current_line.length:
            return current_line.end_point
        elif train.position == 0:
            return current_line.start_point
        return None
