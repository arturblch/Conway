class UpObject:
    def __init__(self, post=[], train=[]):
        self.post = post
        self.train = train

    def update(self, post, train):
        self.post = post
        self.train = train