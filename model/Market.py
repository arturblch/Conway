class Market:
    def __init__(self, post):
        self.idx = post['idx']
        self.name = post['name']
        self.product = post['product']
        if 'product_capacity' in post.keys():
            self.product_capacity = post['product_capacity']
        else:
            self.product_capacity = None
        if 'replenishment' in post.keys():
            self.replenishment = post['replenishment']
        else:
            self.replenishment = None
        self.type = post["type"]

    def __repr__(self):
        return f"Market {self.idx}"

    def update(self, post):               
        self.product = post['product']
