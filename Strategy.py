from model.Objects import Objects
from model.Map import Map
from model.Move import Move
from model.Train import Train


class Strategy:
    def __init__(self, start_data):
        self.home = start_data["home"]["post_id"]
        self.train_ids = [train['idx'] for train in start_data["train"]]
        self.in_progress = True

    def get_moves(self, objects: Objects, map_graph: Map):
        moves = []
        for train_id in self.train_ids:
            train = objects.trains[train_id]
            move = self.get_move(train, map_graph)
            if move:
                moves.append(move)
        return moves

    # Hardcoded strategy
    def get_move(self, train: Train, map_graph: Map):
        if train.speed == 0:
            point = map_graph.get_point(train.line_idx, train.position)
            if point == self.home:
                line, speed = map_graph.departure(self.home, map_graph.get_first_neighbor(self.home))
                return Move(line, speed, train.idx)
            else:
                line, speed = map_graph.departure(point, self.home)
                return Move(line, speed, train.idx)
            # self.in_progress = False
