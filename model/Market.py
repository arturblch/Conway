class Market:
    def __init__(self, post):
        self.idx = post['idx']
        self.name = post['name']
        self.product = post['product']
        self.product_capacity = post['product_capacity']
        self.replenishment = post['replenishment']

    def __repr__(self):
        return f"{self.name}"

    # def update(self, post):               Нужно?
    #     self.product = post['product']
