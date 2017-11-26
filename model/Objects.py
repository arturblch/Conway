from model.Train import Train
from model.Post import Post

class Objects:
    def __init__(self, response):
        self.trains = {train['idx']: Train(train) for train in response['train']}
        self.posts = {post['idx']: Post(post) for post in response['post']}

    def update(self, response):
        for train in response['train']:
            self.trains[train['idx']].update(train)
        self.posts = {post['idx']: Post(post) for post in response['post']}
