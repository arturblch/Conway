from model.Train import Train
from model.Town import Town
from model.Market import Market
from model.Storage import Storage


class Objects:
    def __init__(self, response):
        self.trains = {
            train['idx']: Train(train)
            for train in response['train']
        }
        self.towns = {}
        self.markets = {}
        self.storages = {}
        self.tick = 0
        for post in response['post']:
            if post['type'] == 1:
                self.towns[post['idx']] = Town(post)
            if post['type'] == 2:
                self.markets[post['idx']] = Market(post)
            if post['type'] == 3:
                self.storages[post['idx']] = Storage(post)

        self.score = 0

    def update(self, layer, map_graph, player):
        self._update_trains(layer["train"], map_graph)
        self._update_posts(layer["post"])
        self._update_score(layer["rating"], player)

    def get_score(self):
        return self.score

    def _update_posts(self, posts):
        for post_response in posts:
            if post_response['type'] == 1:
                self.towns[post_response['idx']].update(post_response)
            if post_response['type'] == 2:
                self.markets[post_response['idx']].update(post_response)
            if post_response['type'] == 3:
                self.storages[post_response['idx']].update(post_response)

    def _update_trains(self, trains, map_graph):
        for train_response in trains:
            if train_response["idx"] not in self.trains.keys():
                self.trains.update({
                    train_response["idx"]: Train(train_response)
                })
            train = self.trains[train_response["idx"]]
            train.update(train_response, map_graph)

    def _update_score(self, rating, player):
        print(rating, player.idx)
        self.score = rating[player.idx]['rating']

    def get_enemy_trains(self, my_id):
        return [
            train for train in self.trains.values() if train.player_id != my_id
        ]
        
    def get_my_trains(self, my_id):
        return [
            train for train in self.trains.values() if train.player_id == my_id
        ]