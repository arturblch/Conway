from model.Objects import Objects
from model.Map import Map
from model.Move import Move
from model.Train import Train
import copy


path = {
    1: [2, 12, 2, 1],                               # Small Market
    2: [11, 21, 31, 32, 31, 21, 11, 1]              # Small Storage
}


class Strategy:
    def __init__(self, player, map_graph: Map, objects: Objects):
        self.home = player.home
        self.town = player.town
        self.objects = objects
        self.map = map_graph
        self.trains = player.trains
        self.in_progress = True
        self.population = player.population
        self.step = {1: 0, 2: 0}

    def get_moves(self, ):
        moves = []
        for train in self.trains:
            move = self.get_move(train)
            if move:
                moves.append(move)
        return moves

    def get_move(self, train: Train):
        if train.speed == 0:
            departure_point = path[train.idx][self.step[train.idx]]
            line, speed = self.map.departure(train, departure_point)
            print(f"TRAIN ID: {train.idx} CURRENT: {train.point} NEXT: {departure_point}")
            if self.step[train.idx] < len(path[train.idx]) - 1:
                self.step[train.idx] += 1
            else:
                self.step[train.idx] = 0
            return Move(line.idx, speed, train.idx)

