from model.Objects import Objects
from model.Map import Map
from model.Move import Move
from model.Train import Train
from model.UpObject import UpObject


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
        self.busy_lines = None
        self.busy_points = []

    def get_moves(self):
        self.busy_lines = [train.line_idx for train in self.trains if train.position != 0]
        moves = []
        move_m = self.get_move(self.trains[0], list(self.objects.markets.values()))
        if move_m:
            moves.append(move_m)
        move_s = self.get_move(self.trains[1], list(self.objects.storages.values()))
        if move_s:
            moves.append(move_s)
        return moves

    def get_upgrades(self):
        trains = []
        for train in self.trains:
            if train.level == 1:
                trains.append(train.idx)
        if trains:
            return UpObject([], trains)
        if self.town.armor >= self.town.next_level_price:
            return UpObject([self.town.idx], [])
        if self.town.level >= 2:
            for train in self.trains:
                if train.level == 2 and self.town.armor >= train.next_level_price:
                    return UpObject([], [train.idx, ])

    def get_move(self, train: Train, posts):
        if train.speed == 0:
            if train.goods == train.goods_capacity:
                return self.departure(train, self.home)
            town = self.town
            max_potential = (-town.population, self.home)
            for post in posts:
                potential = self.calc_potential(train, post)
                if potential:
                    if potential > max_potential[0]:
                        max_potential = (potential, post.point)
            arrival_point = max_potential[1]
            print(f"ARRIVAL: {arrival_point}")
            if train.point != arrival_point:
                return self.departure(train, arrival_point)
            else:
                print('WAITING')
                print(f"CURRENT: {train.point} POTENTIAL: {max_potential[0]}")

    def departure(self, train, arrival_point):
        line, speed, next_point = self.map.departure(train, arrival_point, self.busy_lines, self.busy_points)
        print(f"CURRENT: {train.point} NEXT: {next_point}")
        if train.point != self.home:
            self.busy_points.remove(train.point)
        if next_point != self.home:
            self.busy_points.append(next_point)
        # self.busy_lines.append(line.idx)
        return Move(line.idx, speed, train.idx)

    def calc_potential(self, train, post):
        if post.type == 2:
            return self._calc_market_potential(train, post)
        elif post.type == 3:
            return self._calc_storage_potential(train, post)

    def _calc_market_potential(self, train, market):
        distance = self.map.get_distance(train.point, market.point)
        return_distance = self.map.get_distance(market.point, self.home)
        if self.town.product - self.town.population * (distance + return_distance) >= 0:
            potential = min(train.goods + min(market.product + market.replenishment * distance, market.product_capacity), train.goods_capacity)\
                               - self.town.population * (distance + return_distance)
            potential /= distance + return_distance
            return potential

    def _calc_storage_potential(self, train, storage):
        distance = self.map.get_distance(train.point, storage.point)
        return_distance = self.map.get_distance(storage.point, self.home)
        if self.town.product - self.town.population * (distance + return_distance) >= 0:
            potential = min(train.goods + min(storage.armor + storage.replenishment * distance,
                                              storage.armor_capacity), train.goods_capacity) \
                        - self.town.population * (distance + return_distance)
            potential /= distance + return_distance
            return potential
