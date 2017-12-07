import sys
from Strategy import Strategy
from tabulate import tabulate
from RemoteProcessClient import RemoteProcessClient
from GUI import GUI


class Runner:
    def __init__(self, name="Mickey"):
        self.player = None
        self.map_graph = None
        self.objects = None
        self.gui = None

        if len(sys.argv) >= 2 and sys.argv[1] == '-gui':
            self.is_gui = True
        else:
            self.is_gui = False

        self.process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                  443)
        self.name = name

    def run(self):
        try:
            self.player = self.process_client.login(self.name)
            self.map_graph = self.process_client.read_map()
            self.objects = self.process_client.read_objects()
            self.map_graph.define_points(self.objects)
            strategy = Strategy(self.player, self.map_graph, self.objects)
            if self.is_gui:
                self.gui = GUI(self.player, self.map_graph, self.objects)
            while self.player.is_alive:
                self.process_client.update_objects(self.objects, self.map_graph.lines)
                self.print_state()
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

    def move(self, strategy):
        moves = strategy.get_moves()
        if moves:
            for move in moves:
                self.process_client.move(move)
        self.process_client.turn()

    def print_state(self):
        str_post = []
        for town in self.objects.towns.values():
            str_post.append([town.name, town.product, town.population])
        for market in self.objects.markets.values():
            str_post.append([market.name, market.product, '-'])

        print(tabulate(str_post, headers=['name', 'products', 'population']), '\n')

        for train in self.objects.trains.values():
            print(
                    tabulate(
                        [[
                            train.idx, train.goods, train.line_idx, train.speed,
                            train.position
                        ]],
                        headers=[
                            'Train_id', 'product', 'line_idx', 'speed', 'position'
                        ]))


if __name__ == '__main__':
    Runner().run()
