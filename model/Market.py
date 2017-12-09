# "event": [],
# "idx": 3,
# "name": "market-medium",
# "point_id": 49,
# "product": 250,
# "product_capacity": 250,
# "replenishment": 10,
# "type": 2


class Market:
    def __init__(self, post):
        self.event = post['event']
        self.idx = post['idx']
        self.name = post['name']
        self.point = post['point_id']
        self.product = post['product']
        self.product_capacity = post['product_capacity']
        self.replenishment = post['replenishment']
        self.type = post["type"]

    def update(self, post):
        self.event = post['event']
        self.product = post['product']

    def __repr__(self):
        return f"{self.name}"
