class Train:
    def __init__(self, response):
        self.capacity = response['capacity']
        self.idx = response['idx']
        self.line_idx = response['line_idx']
        self.player_id = response['player_id']
        self.position = response['position']
        self.product = response['product']
        self.speed = response['speed']

    def update(self, response):
        self.line_idx = response['line_idx']
        self.position = response['position']
        self.product = response['product']
        self.speed = response['speed']
