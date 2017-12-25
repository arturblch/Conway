import sys
from Strategy_new import Strategy
from tabulate import tabulate
from RemoteProcessClient import RemoteProcessClient
from model.LoginError import LoginError
from GUI import GUI
from time import sleep


class Runner:
    def __init__(self, name="player1"):
        self.player = None
        self.map_graph = None
        self.objects = None
        self.is_gui = True
        self.game = 'Conway'
        self.num_players = 2
        self.multi = False
        self.name = name
        if len(sys.argv) >= 2:
            if '-gui' in sys.argv:
                self.is_gui = True
            if '-m' in sys.argv:
                self.multi = True
                self.name = input("Name:")
                self.game = input("Game name:")
                self.num_players = int(input("Num of players:"))
        self.process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                  443)

    def run(self):
        try:
            try:
                if self.multi == False:
                    self.player = self.process_client.login(self.name, self.num_players, self.game)
                else:
                    self.player = self.process_client.login(self.name, self.num_players, self.game)
            except LoginError:
                self.process_client.logout()
                print('BAD LOGIN\nTRY AGAIN')
                exit()
            self.init_world()
            strategy = Strategy(self.player, self.map_graph, self.objects)
            if self.is_gui:
                self.gui = GUI(self.player, self.map_graph, self.objects, strategy)
            while self.player.is_alive:
                self.process_client.update_objects(self.objects,
                                                   self.map_graph, self.player)
                # self.print_state()
                if self.is_gui:
                    self.gui.turn()
                    if (not self.gui.paused) or self.gui.onestep:
                        self.move(strategy)
                else:
                    self.move(strategy)
        finally:
            self.process_client.logout()
            self.process_client.close()

        return self.player.is_alive  # for testing

    def init_world(self):
        self.map_graph = self.process_client.read_map()
        self.map_graph.pos = dict(
            [(cord['idx'], (cord['x'] / 200, cord['y'] / 200))
             for cord in self.process_client.read_position()["coordinate"]])
        self.objects = self.process_client.read_objects()
        # self.map_graph.define_points(self.objects)
        self.player.settle(self.map_graph, self.objects)

    def move(self, strategy):  # move == ход
        moves = strategy.get_moves()
        if moves:
            for move in moves:
                self.process_client.move(move)
        up_obj = strategy.get_upgrade()
        if up_obj:
            self.process_client.upgrade(up_obj)
        self.process_client.turn()
        self.objects.tick += 1

    def print_state(self):
        str_post = []
        for town in self.objects.towns.values():
            str_post.append(
                [town.name, town.product, town.armor, town.population])
        for market in self.objects.markets.values():
            str_post.append([market.name, market.product, '-', '-'])
        for storage in self.objects.storages.values():
            str_post.append([storage.name, '-', storage.armor, '-'])

        print(
            tabulate(
                str_post, headers=['name', 'product', 'armor', 'population']),
            '\n')

        for train in self.objects.trains.values():
            print(
                tabulate(
                    [[
                        train.idx, train.goods, train.post_type,
                        train.line_idx, train.speed, train.position
                    ]],
                    headers=[
                        'Train_id', 'product', 'post_type', 'line_idx',
                        'speed', 'position'
                    ]))


if __name__ == '__main__':
    Runner().run()
