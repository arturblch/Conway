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
            train.arrival()
            if train.position is None:                                                  # Если поезд ещё не начинал путь
                train.departure(self.home, map_graph.get_first_neighbor(self.home))     # Отправляем его к первому соседнему городу
                line = map_graph.get_line(train.departure_point, train.arrival_point)
                return Move(line, 1, train.idx)
            if train.current_point != self.home:                                        # Если поезд прибыл не домой
                train.departure(train.current_point, self.home)                         # Отправляем поезд домой
                line = map_graph.get_line(train.departure_point, train.arrival_point)
                return Move(line, 1, train.idx)
            self.in_progress = False
