# "armor": 100,
# "armor_capacity": 100,
# "level": 1,
# "next_level_price": 100,
# "population": 3,
# "population_capacity": 10,
# "product": 350,
# "product_capacity": 200,

# "player_id": "92b23d2f-81ae-4c2d-b4e5-aa81f70fda8e",
# "point_id": 1,
# "event": [],
# "idx": 1,
# "name": "town-one",
# "type": 1


class Town:
    def __init__(self, post):
            # id properties 
        self.idx = post["idx"]
        self.player_id = post["player_id"]
        self.point_id = post["point_id"]
            # other properties
        self.name = post["name"]
        self.type = post["type"]
        self.event = post['event']
            # armor properties
        self.armor = post["armor"]
        self.armor_capacity = post["armor_capacity"]
            # population properties
        self.population = post["population"]
        self.population_capacity = post["population_capacity"]
            # product properties
        self.product = post["product"]
        self.product_capacity = post["product_capacity"]
            # level properties
        self.level = post["level"]
        self.next_level_price = post["next_level_price"]

    def update(self, post):
        self.armor = post["armor"]
        self.armor_capacity = post["armor_capacity"]

        self.population = post["population"]
        self.population_capacity = post["population_capacity"]

        self.product = post["product"]
        self.product_capacity = post["product_capacity"]

        self.level = post["level"]
        self.next_level_price = post["next_level_price"]

        self.event = post['event']