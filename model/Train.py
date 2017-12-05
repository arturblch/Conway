class Train:
    def __init__(self, response):
        self.event = response['event']
        self.goods = response['goods']
        self.goods_capacity = response["goods_capacity"]
        self.idx = response['idx']
        self.level = response["level"]
        self.line_idx = response['line_idx']
        self.next_level_price = response["next_level_price"]
        self.player_id = response['player_id']
        self.position = response['position']
        self.post_type = response["post_type"]
        self.speed = response['speed']
        self.node = None


    def update_node(self, lines):
        cur_line = lines[self.line_idx]

        if self.position == cur_line.length:
            self.node = cur_line.end_point
        elif self.position == 0:
            self.node = cur_line.start_point
        else:
            self.node = None

    def update(self, response):
        self.line_idx = response['line_idx']
        self.position = response['position']
        self.goods = response['goods']
        self.speed = response['speed']