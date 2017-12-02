from model.Train import Train
from model.Town import Town
from model.Market import Market


class Objects:
    def __init__(self, response): # lines for trains
        self.trains = {
            train['idx']: Train(train)
            for train in response['train']
        }
        self.towns = {}
        self.markets = {}
        for post in response['post']:
            if post['type'] == 1:
                self.towns[post['idx']] = Town(post)
            if post['type'] == 2:
                self.markets[post['idx']] = Market(post)

    def update_trains_node(self, lines):
        if lines:
            for train in self.trains.values():
                train.update_node(lines)
