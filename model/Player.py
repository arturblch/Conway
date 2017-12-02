# Лучшие времена
from model.Point import Point

class Player:
    def __init__(self, response=None):
        if response['home'] != None:
            self.home = Point(**response['home'])
        else:
            self.home = None
        self.idx = response['idx']
        self.name = response['name']
        if response['train']:
            self.trains = [train['idx'] for train in response['train']]
        else:
            self.trains = None
        self.is_alive = True
