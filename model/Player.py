from model.LoginError import LoginError


class Player:
    def __init__(self, response):
        if response['home'] is None:
            raise LoginError('Bad login')
        self.home = response['home']['idx']
        self.town = response['town']["idx"]
        self.population = response["town"]["population"]
        self.idx = response['idx']
        self.name = response['name']
        if response['train']:
            self.trains = [train['idx'] for train in response['train']]
        else:
            self.trains = None
        self.is_alive = True

    def settle(self, map_graph, objects):
        self.town = objects.towns[self.town]
        self.trains = [objects.trains[train_id] for train_id in self.trains]
