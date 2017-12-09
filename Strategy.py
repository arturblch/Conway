from model.Objects import Objects
from model.Map import Map
from model.Move import Move
from model.Train import Train
import copy


class Strategy:
    def __init__(self, player_data, map_graph: Map, objects: Objects):
        self.home = player_data.home
        self.town = player_data.town
        self.objects = objects
        self.map = map_graph
        self.train_ids = player_data.trains
        self.in_progress = True
        self.population = player_data.population
        self.best_way = [], 0   # way through markets, product growth on per move

    def get_moves(self, ):
        moves = []
        for train_id in self.train_ids:
            train = self.objects.trains[train_id]
            move = self.get_move(train)
            if move:
                moves.append(move)
        return moves

    def move_to_point(self, train, arrival_point, offset=0):
        if train.point is None:
            line = self.map.lines[train.line_idx]
        else:
            line = self.map.Graph.edges(train.point, arrival_point)
            if line is None:
                return
        need_pos = 0 + offset if line.start_point == arrival_point \
                                  else line.length - offset

        if need_pos > train.position:
            speed = 1
        elif need_pos < train.position:
            speed = -1
        else:
            speed = 0
        return Move(line.idx, speed, train.idx)

    def get_move(self, train: Train):
        if train.speed == 0:
            current_point = train.point
            if len(self.best_way[0]) == 0:
                if current_point != self.home:
                    next_point = self.map.get_next_point(current_point.idx, self.home)
                    line, speed = self.map.departure(current_point.idx, next_point.idx)
                    print(f"CURRENT: {current_point} NEXT: {next_point}")
                    return Move(line.idx, speed, train.idx)
                else:
                    self.best_way = [], 0
                    markets = {market: market.product for market in self.objects.markets.values()}
                    self.build_path(markets, self.town.product, train.goods, 0)
            market = self.best_way[0][0]
            market_point = market.point
            next_point = self.map.get_next_point(current_point, market_point)
            line, speed = self.map.departure(current_point, next_point)
            if next_point == market_point:
                self.best_way[0].pop(0)
            print(f"CURRENT: {current_point} NEXT: {next_point}")
            return Move(line.idx, speed, train.idx)
            # self.in_progress = False

    def build_path(self, markets, product, train_prod, total_distance, path=None):
        if path is None:
            path = []
            current_point = self.home
        else:
            current_point = path[-1].point
        if current_point is None:
            current_point = self.home
        for market in markets:
            market_point = market.point
            distance = self.map.get_distance(current_point, market_point)
            return_distance = self.map.get_distance(market_point, self.home)
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

