from model.Train import Train
from model.Town import Town
from model.Market import Market


class Objects:
    def __init__(self, response):
        self.trains = {train['idx']: Train(train) for train in response['train']}
        self.posts = {}
        for post in response['post']:
            if post['type'] == 1:
                self.posts[post['idx']] = Town(post)
            if post['type'] == 2:
                self.posts[post['idx']] = Market(post)
