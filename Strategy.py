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
            # max_potential = (town.product-town.population, map_graph.get_point(1, 0))  # home point
            max_potential = (0, map_graph.get_point(1, 0))  # home point
            for market in markets.values():
                market_point = map_graph.get_market_point(market)
                if market_point == current_point:
                    continue
                distance = map_graph.get_distance(current_point.idx, market_point.idx)
                return_distance = map_graph.get_distance(market_point.idx, self.home)
                if town.product - town.population*(distance+return_distance) >= town.population:
                    market_potential = min(market.product + market.replenishment*distance, market.product_capacity) - \
                                       town.population*(distance+return_distance) + town.product + train.product
                    print((market_potential, market), max_potential)
                    if market_potential > max_potential[0]:
                        max_potential = (market_potential, market_point)
            arrival_point = max_potential[1]
            if current_point != arrival_point:
                next_point = map_graph.get_next_point(current_point.idx, arrival_point.idx)
                line, speed = map_graph.departure(current_point.idx, next_point.idx)
                print(f"CURRENT: {current_point} NEXT: {next_point}")
                return Move(line.idx, speed, train.idx)
            else:
                print('WAITING :(')
                print(f"CURRENT: {current_point} POTENTIAL: {max_potential[0]}")
            # self.in_progress = False
