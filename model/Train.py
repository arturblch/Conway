class Train:
    def __init__(self, response):
        self.capacity = response['capacity']
        self.idx = response['idx']
        self.line_idx = response['line_idx']
        self.player_id = response['player_id']
        self.position = response['position']
        self.product = response['product']
        self.speed = response['speed']
        self.departure_point = None
        self.arrival_point = None
        self.current_point = None

    def departure(self, departure_point, arrival_point):
        self.current_point = None
        self.departure_point = departure_point
        self.arrival_point = arrival_point

    def arrival(self):
        self.current_point = self.arrival_point
        self.arrival_point = None
        self.departure_point = None

    def update(self, response):
        self.capacity = response['capacity']
        self.idx = response['idx']
        self.line_idx = response['line_idx']
        self.player_id = response['player_id']
        self.position = response['position']
        self.product = response['product']
        self.speed = response['speed']
