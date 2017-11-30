# Лучшие времена
from model.Point import Point

class Player:
    def __init__(self, response):
        if response['home'] != None:
            self.home = Point(**response['home'])
        else:
            self.home = None
        self.idx = response['idx']
        self.name = response['name']
        self.trains = [train['idx'] for train in response['train']]
        self.is_alive = True
