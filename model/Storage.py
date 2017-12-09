# "armor": 20,
# "armor_capacity": 20,
# "event": [],
# "idx": 5,
# "name": "storage-small",
# "point_id": 32,
# "replenishment": 1,
# "type": 3


class Storage:
    def __init__(self, post):
        self.event = post['event']
        self.idx = post['idx']
        self.name = post['name']
        self.point = post['point_id']
        self.armor = post['armor']
        self.armor_capacity = post['armor_capacity']
        self.replenishment = post['replenishment']
        self.type = post["type"]

    def update(self, post):
        self.event = post['event']
        self.armor = post['armor']

    def __repr__(self):
        return f"{self.name}"
