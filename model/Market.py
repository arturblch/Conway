class Market:
    def __init__(self, post):
        self.idx = post['idx']
        self.name = post['name']
        self.product = post['product']
        self.product_capacity = post['product_capacity']
        self.replenishment = post['replenishment']
        self.type = post["type"]

    def __repr__(self):
        return f"Market {self.idx}"

    def update(self, post):               
        self.product = post['product']
