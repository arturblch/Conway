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
        for post in response['post']:
            if post['type'] == 1:
                self.towns[post['idx']] = Town(post)
            if post['type'] == 2:
                self.markets[post['idx']] = Market(post)
            if post['type'] == 3:
                self.storages[post['idx']] = Storage(post)

    def update(self, layer, map_graph):
        self._update_trains(layer["train"], map_graph)
        self._update_posts(layer["post"])

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
            if train_response["idx"] in self.trains:
                train = self.trains[train_response["idx"]]
                train.update(train_response, map_graph)
            else:
                self.trains[train_response["idx"]] = Train(train_response)
