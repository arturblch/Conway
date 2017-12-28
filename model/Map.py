import networkx as nx
from model.Line import Line


class Map:
    def __init__(self, response):
        self.Graph = nx.Graph()
        self.lines = {line['idx']: Line(**line) for line in response["line"]}
        self.points = [point['idx'] for point in response["point"]]
        self.posts = {
            point['post_id']: point['idx']
            for point in response["point"] if point['post_id'] is not None
        }
        self.Graph.add_nodes_from(self.points)
        self.Graph.add_edges_from([(*line['point'], {
            'length': line['length'],
            'line': Line(**line)
        }) for line in response["line"]])

        self.pos = None

        self.pos = nx.spring_layout(
            self.Graph,
            scale=0.5,
            center=(0.5, 0.5),
            iterations=200,
            weight="length")

    def get_neighbors(self, point):
        return list(self.Graph.neighbors(point))

    # def define_points(self, objects):
    #     posts = list(objects.towns.values()) + list(objects.markets.values()) + list(objects.storages.values())
    #     for post in posts:
    #         post.point = self.points[post.point_id]

    # TODO:
    # 1. delete departure_point (departure_point == train.point)
    # 2. add departure from any position of the line
    def departure(self, departure_point,
                  arrival_point):  # можно преоразовать сразу в Move
        print(departure_point, arrival_point)
        line = self.Graph.get_edge_data(departure_point, arrival_point)['line']
        speed = 1 if line.start_point == departure_point else -1
        return line, speed

    def get_distance(self, u, v):
        return nx.shortest_path_length(
            self.Graph, source=u, target=v, weight='length')

    def distance_to_all_targets(self, source, targets):
        distance_list = [(self.distance_pos_pos(source, target), target)
                         for target in targets]
        distance_list = sorted(distance_list,  key=lambda x: x[0])
        return distance_list


    def get_distance_from_line(self, line_idx, pos, point):
        line = self.lines[line_idx]
        return min(
            self.get_distance(line.start_point, point) + pos,
            self.get_distance(line.end_point, point) + line.length - pos)

    def distance_pos_pos(self, from_pos, to_pos):
        if from_pos.point != None:
            return self.get_distance(from_pos.point, to_pos.point)
        else:
            return self.get_distance_from_line(from_pos.line, from_pos.pos,
                                                   to_pos.point)

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

    def get_point(self, line_idx, posit):
        line = self.lines[line_idx]
        if posit == line.length:
            return line.end_point
        elif posit == 0:
            return line.start_point
        return None

    def get_neighbors_pos(self, pos):
        nb_pos = []

        if pos.point != None:
            nb = self.Graph.neighbors(pos.point)
            nb_lines = [
                self.Graph.get_edge_data(pos.point, nb_point)['line']
                for nb_point in nb
            ]
            for line in nb_lines:
                posit = line.length - 1 if pos.point == line.end_point else 1
                point = self.get_point(line.idx, posit)
                nb_pos.append(Position(point, line.idx, posit))
        else:
            pos_1 = pos.pos - 1
            point_1 = self.get_point(pos.line, pos_1)
            nb_pos.append(Position(point_1, pos.line, pos_1))

            pos_2 = pos.pos + 1
            point_2 = self.get_point(pos.line, pos_2)
            nb_pos.append(Position(point_2, pos.line, pos_2))

        return nb_pos


class Position:
    def __init__(self, point=None, line=None, pos=None, train=None):
        if train is None:
            self.point = point
            self.line = line
            self.pos = pos
        else:
            self.point = train.point
            self.line = train.line_idx
            self.pos = train.position

    def __eq__(self, other):
        return (self.point != None and self.point == other.point
                or self.line != None and self.line == other.line
                and self.pos == other.pos)

    def __repr__(self):
        return 'p - {}, l - {}, pos - {}'.format(self.point, self.line,
                                                 self.pos)

    def __hash__(self):
        if self.point != None:
            return hash((self.point, None, None))
        else:
            return hash((None, self.line, self.pos))
