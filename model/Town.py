class Town:
    def __init__(self, post):
        self.name = post["name"]
        self.armor = post["armor"]
        self.population = post["population"]
        self.product = post["product"]
        self.type = post["type"]

    def update(self, post):
        self.armor = post["armor"]
        self.population = post["population"]
        self.product = post["product"]
        self.product = post["product"]