# Лучшие времена
from model.Point import Point

class Player:
    def __init__(self, response):
        self.home = Point(response['home'])
        self.idx = response['home']idx
        self.name = response['home']name
        self.trains = [train['idx'] for train in response['train']]
