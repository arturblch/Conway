class Market:
    def __init__(self, post):
        self.name = post['name']
        self.product = post['product']
    
    def update(self, post):
        self.product = post['product']