from model.Point import Point


class Player:
    def __init__(self, response=None):
        if response['home'] is not None:
            self.home = Point(**response['home'])
        else:
            self.home = None
        self.town = response['town']["idx"]
        self.population = response["town"]["population"]
        self.idx = response['idx']
        self.name = response['name']
        if response['train']:
            self.trains = [train['idx'] for train in response['train']]
        else:
            self.trains = None
        self.is_alive = True
