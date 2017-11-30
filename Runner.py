import sys
from Strategy import Strategy
from RemoteProcessClient import RemoteProcessClient


class Runner:
    def __init__(self):
        if sys.argv.__len__() == 4:
            self.remote_process_client = RemoteProcessClient(sys.argv[1], int(sys.argv[2]))
            self.name = sys.argv[3]
        else:
            self.remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net', 443)
            self.name = "Mickey"

    def run(self):
        status, player_data = self.remote_process_client.login(self.name)
        try:
            map_graph = self.remote_process_client.read_map()
            strategy = Strategy(player_data)
            # while strategy.in_progress:
            for _ in range(30):
                objects = self.remote_process_client.read_objects()
                moves = strategy.get_moves(objects, map_graph)
                if moves:
                    for move in moves:
                        self.remote_process_client.move(move)
                self.remote_process_client.turn()
        finally:
            self.remote_process_client.logout()
            self.remote_process_client.close()


if __name__ == '__main__':
    Runner().run()
