import sys
from Strategy_2 import Strategy_2
from RemoteProcessClient import RemoteProcessClient
from GUI import GUI


class Runner:
    def __init__(self):

        if sys.argv[2] == '-gui':
            self.is_gui = True
        else:
            self.is_gui = False

        self.remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net', 443)
        self.name = "Mickey"

    def run(self):
        player = self.remote_process_client.login(self.name)
        try:
            map_graph = self.remote_process_client.read_map()
            objects = self.remote_process_client.read_objects()
            strategy = Strategy_2(player, map_graph, objects)
            if self.is_gui:
                self.gui = GUI(map_graph, objects)
            while player.is_alive:
                self.remote_process_client.update_objects(strategy.objects)

                moves = strategy.get_moves()
                if moves:
                    for move in moves:
                        self.remote_process_client.move(move)
                if self.is_gui:
                    self.gui.turn()
                self.remote_process_client.turn()
        finally:
            self.remote_process_client.logout()
            self.remote_process_client.close()


if __name__ == '__main__':
    Runner().run()
