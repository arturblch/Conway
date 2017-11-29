class Town:
    def __init__(self, post):
        self.name = post["name"]
        self.armor = post["armor"]
        self.population = post["population"]
        self.product = post["product"]

    # def update(self, post):             Нужно?
    #     self.armor = post["armor"]
    #     self.population = post["population"]
    #     self.product = post["product"]
