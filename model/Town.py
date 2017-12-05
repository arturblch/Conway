class Town:
    def __init__(self, post):
        self.name = post["name"]
        self.armor = post["armor"]
        self.event = post['event']
        self.population = post["population"]
        self.product = post["product"]
        self.type = post["type"]
        self.armor_capacity = post["armor_capacity"]
        self.level = post["level"]
        self.next_level_price = post["next_level_price"]
        self.point_id = post["point_id"]
        self.population_capacity = post["population_capacity"]
        self.product_capacity = post["product_capacity"]

    def update(self, post):
        self.armor = post["armor"]
        self.event = post['event']
        self.population = post["population"]
        self.next_level_price = post["next_level_price"]
        self.level = post["level"]
        self.product = post["product"]

