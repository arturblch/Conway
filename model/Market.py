class Market:
    def __init__(self, post):
        self.name = post['name']
        self.product = post['product']
        self.replenishment = post['replenishment']

    # def update(self, post):               Нужно?
    #     self.product = post['product']
