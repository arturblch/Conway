import sys
from Strategy_2 import Strategy
from LocalProcessClient import ProcessClient
from GUI import GUI


class Runner:
    def __init__(self):

        if len(sys.argv) >=2 and sys.argv[1] == '-gui':
            self.is_gui = True
        else:
            self.is_gui = False

        self.process_client = ProcessClient()

    def run(self):
        player = self.process_client.login(1)
        map_graph = self.process_client.read_map()
        objects = self.process_client.read_objects()
        strategy = Strategy(player, map_graph, objects)
        if self.is_gui:
            self.gui = GUI(player, map_graph, objects)
        i = 300
        while player.is_alive:
            objects = self.process_client.read_objects()
            if self.is_gui:
                self.gui.update_objects(objects)
            moves = strategy.get_moves()
            if moves:
                for move in moves:
                    print(move.speed)
                    self.process_client.move(move)
            if self.is_gui:
                while(self.gui.paused):
                    self.gui.turn()
            self.process_client.turn()
            if i != 0:
                i -=1
            else:
                player.is_alive = False


        return player.is_alive                  # for testing


if __name__ == '__main__':
    Runner().run()
