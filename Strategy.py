from model.Objects import Objects
from model.Map import Map
from model.Move import Move
from model.Train import Train


class Strategy:
    def __init__(self, player_data):
        self.home = player_data["home"]["post_id"]
        self.town = player_data["town"]["idx"]
        self.train_ids = [train['idx'] for train in player_data["train"]]
        self.in_progress = True
        self.population = player_data["town"]["population"]
        self.best_way = [], 0   # way through markets, product growth on each move

    def get_moves(self, objects: Objects, map_graph: Map):
        moves = []
        for train_id in self.train_ids:
            train = objects.trains[train_id]
            move = self.get_move(train, objects, map_graph)
            if move:
                moves.append(move)
        return moves

    def get_move(self, train: Train, objects: Objects, map_graph: Map):
        if train.speed == 0:
            current_point = map_graph.get_point(train.line_idx, train.position)
            if len(self.best_way[0]) == 0:
                if current_point.idx != self.home:
                    next_point = map_graph.get_next_point(current_point.idx, self.home)
                    line, speed = map_graph.departure(current_point.idx, next_point.idx)
                    print(f"CURRENT: {current_point} NEXT: {next_point}")
                    return Move(line.idx, speed, train.idx)
                else:
                    self.best_way = [], 0
                    town = objects.towns[self.town]
                    markets = {market: market.product for market in objects.markets.values()}
                    self.build_path(map_graph, markets, town.product, train.product, 0)
            market = self.best_way[0][0]
            market_point = map_graph.get_market_point(market)
            next_point = map_graph.get_next_point(current_point.idx, market_point.idx)
            line, speed = map_graph.departure(current_point.idx, next_point.idx)
            if next_point == market_point:
                self.best_way[0].pop(0)
            print(f"CURRENT: {current_point} NEXT: {next_point}")
            return Move(line.idx, speed, train.idx)
            # self.in_progress = False

    def build_path(self, map_graph: Map, markets, product, train_prod, total_distance, path=None):
        # home_point = map_graph.get_point(1, 0)
        home_point = map_graph.get_post(self.home)
        if path is None:
            path = []
            current_point = home_point
        else:
            current_point = map_graph.get_market_point(path[-1])
        for market in markets:
            market_point = map_graph.get_market_point(market)
            distance = map_graph.get_distance(current_point.idx, market_point.idx)
            return_distance = map_graph.get_distance(market_point.idx, home_point.idx)
            if product - self.population*(distance+return_distance) >= 0:
                new_total_distance = total_distance + distance
                new_train_prod = train_prod + markets[market]
                new_markets = markets.copy()
                new_path = path.copy()
                if path:
                    m = path[-1]
                    new_markets.update({m: min(m.product + m.replenishment*distance, m.product_capacity)})
                new_markets.pop(market)
                new_path.append(market)
                for m in new_markets:
                    new_markets.update({m: min(m.product + m.replenishment*distance, m.product_capacity)})
                profit = new_train_prod / (return_distance + new_total_distance)
                if profit >= self.best_way[1]:
                    self.best_way = new_path, profit
                # print(new_path, profit)
                # print(self.best_way)
                self.build_path(map_graph, new_markets, product-self.population*distance, new_train_prod, new_total_distance, new_path)

