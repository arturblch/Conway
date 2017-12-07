from model.Objects import Objects
from model.Map import Map
from model.Move import Move
from model.Train import Train
import copy


class Strategy:
    def __init__(self, player_data, map_graph: Map, objects: Objects):
        self.home = player_data.home.post_id
        self.town = player_data.town
        self.objects = objects
        self.map = map_graph
        self.train_ids = player_data.trains
        self.in_progress = True
        self.population = player_data.population
        self.best_way = [], 0   # way through markets, product growth on each move

    def get_moves(self, ):
        moves = []
        for train_id in self.train_ids:
            train = self.objects.trains[train_id]
            move = self.get_move(train)
            if move:
                moves.append(move)
        return moves

    def get_move(self, train: Train):
        if train.speed == 0:
            current_point = self.map.points[train.point]
            if len(self.best_way[0]) == 0:
                if current_point.idx != self.home:
                    next_point = self.map.get_next_point(current_point.idx, self.home)
                    line, speed = self.map.departure(current_point.idx, next_point.idx)
                    print(f"CURRENT: {current_point} NEXT: {next_point}")
                    return Move(line.idx, speed, train.idx)
                else:
                    self.best_way = [], 0
                    town = self.objects.towns[self.town]
                    markets = {market: market.product for market in self.objects.markets.values()}
                    self.build_path(markets, town.product, train.goods, 0)
            market = self.best_way[0][0]
            market_point = market.point
            next_point = self.map.get_next_point(current_point.idx, market_point.idx)
            line, speed = self.map.departure(current_point.idx, next_point.idx)
            if next_point == market_point:
                self.best_way[0].pop(0)
            print(f"CURRENT: {current_point} NEXT: {next_point}")
            return Move(line.idx, speed, train.idx)
            # self.in_progress = False

    def build_path(self, markets, product, train_prod, total_distance, path=None):
        # home_point = map_graph.get_point(1, 0)
        home_point = self.map.points[self.home]
        if path is None:
            path = []
            current_point = home_point
        else:
            current_point = path[-1].point
        for market in markets:
            market_point = market.point
            distance = self.map.get_distance(current_point.idx, market_point.idx)
            return_distance = self.map.get_distance(market_point.idx, home_point.idx)
            if (product - self.population*(distance+return_distance)) >= 0 and (len(path) <= 5):
                new_total_distance = total_distance + distance
                new_train_prod = train_prod + markets[market]
                new_markets = markets.copy()
                new_path = path.copy()
                new_market = copy.copy(market)
                new_market.product = 0
                if path:
                    m = path[-1]
                    new_markets.update({m: min(m.product + m.replenishment*distance, m.product_capacity)})
                new_markets.pop(market)
                new_path.append(new_market)
                for m in new_markets:
                    new_markets.update({m: min(m.product + m.replenishment*distance, m.product_capacity)})
                profit = new_train_prod / (return_distance + new_total_distance)
                if profit >= self.best_way[1]:
                    self.best_way = new_path, profit
                # print(new_path, profit)
                # print(self.best_way)
                self.build_path(new_markets, product-self.population*distance, new_train_prod, new_total_distance, new_path)

