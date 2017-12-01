import sys
from Strategy_2 import Strategy
from RemoteProcessClient import RemoteProcessClient
from GUI import GUI


class Runner:
    def __init__(self, name="Mickey"):

        if len(sys.argv)>=2 and sys.argv[1] == '-gui':
            self.is_gui = True
        else:
            self.is_gui = False

        self.remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net', 443)
        self.name = name

    def run(self):
        try:
            player = self.remote_process_client.login(self.name)
            map_graph = self.remote_process_client.read_map()
            objects = self.remote_process_client.read_objects()
            strategy = Strategy(player, map_graph, objects)
            if self.is_gui:
                self.gui = GUI(player, map_graph, objects)
            i = 30
            while player.is_alive:
                self.remote_process_client.update_objects(strategy.objects)

                moves = strategy.get_moves()
                if moves:
                    for move in moves:
                        self.remote_process_client.move(move)
                if self.is_gui:
                    self.gui.turn()
                self.remote_process_client.turn()
                if i!=0:
                    i -=1
                else:
                    player.is_alive = False
        finally:
            self.remote_process_client.logout()
            self.remote_process_client.close()

        return player.is_alive                  # for testing


if __name__ == '__main__':
    Runner().run()
