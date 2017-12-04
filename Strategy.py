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
        self.best_way = [], 0   # way through markets, product count after return

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
            markets = objects.markets
            town = objects.towns[self.town]

            # if current_point.idx != self.home:
            #     distance = map_graph.get_distance(current_point.idx, self.home)
            # else:
            #     distance = 1
            # max_potential = (town.product - town.population*distance + train.product, map_graph.get_point(1, 0))

            max_potential = (0, map_graph.get_point(1, 0))
            for market in markets.values():
                market_point = map_graph.get_market_point(market)
                if market_point == current_point:
                    continue
                distance = map_graph.get_distance(current_point.idx, market_point.idx)
                return_distance = map_graph.get_distance(market_point.idx, self.home)
                if town.product - town.population*(distance+return_distance) >= 0:
                    market_potential = min(market.product + market.replenishment*distance, market.product_capacity) - \
                                       town.population*(distance+return_distance) + town.product + train.product
                    print((market_potential, market), max_potential)
                    if market_potential > max_potential[0]:
                        max_potential = (market_potential, market_point)
            arrival_point = max_potential[1]
            print(f"ARRIVAL: {arrival_point}")
            if current_point != arrival_point:
                # print(current_point, arrival_point)
                next_point = map_graph.get_next_point(current_point.idx, arrival_point.idx)
                line, speed = map_graph.departure(current_point.idx, next_point.idx)
                print(f"CURRENT: {current_point} NEXT: {next_point}")
                return Move(line.idx, speed, train.idx)
            else:
                print('WAITING :(')
                print(f"CURRENT: {current_point} POTENTIAL: {max_potential[0]}")
            # self.in_progress = False

    def choose_path(self, map_graph: Map, markets, product, train_prod, path=None):
        home = map_graph.get_point(1, 0)
        if path is None:
            path = []
            current_point = home
        else:
            current_point = map_graph.get_market_point(path[-1])
        for market in markets:
            market_point = map_graph.get_market_point(market)
            distance = map_graph.get_distance(current_point.idx, market_point.idx)
            return_distance = map_graph.get_distance(market_point.idx, home.idx)
            if product - 3*(distance+return_distance) >= 0:
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
                # print(new_markets)
                total_prod = product-3*distance + new_train_prod - 3*return_distance
                # print(total_prod, self.best_way[1])
                if total_prod >= self.best_way[1]:
                    self.best_way = new_path, total_prod
                # print(new_path, total_prod)
                self.choose_path(map_graph, new_markets, product-3*distance, new_train_prod, new_path)

