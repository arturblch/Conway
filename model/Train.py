# "event": [],
# "goods": 0,
# "goods_capacity": 40,
# "idx": 1,
# "level": 1,
# "next_level_price": 40,
# "line_idx": 1,
# "player_id": "92b23d2f-81ae-4c2d-b4e5-aa81f70fda8e",
# "position": 0,
# "post_type": null,
# "speed": 0


class Train:
    def __init__(self, response):
        # id
        self.idx = response['idx']
        self.player_id = response['player_id']
        # goods
        self.goods = response['goods']
        self.goods_capacity = response["goods_capacity"]
        # level
        self.level = response["level"]
        self.next_level_price = response["next_level_price"]
        # movement properties
        self.post_type = response["post_type"]
        self.line_idx = response['line_idx']
        self.position = response['position']
        self.speed = response['speed']
        self.event = response['event']
        self.point = None

    def update(self, response, map_graph):
        # goods
        self.goods = response['goods']
        self.goods_capacity = response["goods_capacity"]
        # level
        self.level = response["level"]
        self.next_level_price = response["next_level_price"]
        # movement properties
        self.post_type = response["post_type"]
        self.line_idx = response['line_idx']
        self.position = response['position']
        self.speed = response['speed']
        self.event = response['event']
        self.point = map_graph.get_train_point(self)
