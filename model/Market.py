class Market:
    def __init__(self, post):
        self.event = post['event']
        self.idx = post['idx']
        self.name = post['name']
        self.point_id = post['point_id']
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

    def update(self, post):
        self.product = post['product']

    def __repr__(self):
        return f"Market {self.idx}"
