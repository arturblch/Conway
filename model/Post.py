class Post:
    def __init__(self, response):
        self.type = response['type']
        if self.type == 1:
            self.armor = response['armor']
            self.idx = response['idx']
            self.name = response['name']
            self.population = response['population']
            self.product = response['product']

        if self.type == 2:
            self.idx = response['idx']
            self.name = response['name']
            self.product = response['product']
