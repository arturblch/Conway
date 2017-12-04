import sys
from time import sleep
from Strategy import Strategy
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
        player = self.process_client.login(2)
        map_graph = self.process_client.read_map()
        objects = self.process_client.read_objects()
        strategy = Strategy(player, map_graph, objects)
        if self.is_gui:
            self.gui = GUI(player, map_graph, objects)
            
        while player.is_alive:
            if self.is_gui:
                self.gui.turn()
                if((not self.gui.paused) or self.gui.onestep):
                    moves = strategy.get_moves()
                    if moves:
                        for move in moves:
                            self.process_client.move(move)
                    self.process_client.turn()
            else:
                moves = strategy.get_moves()
                if moves:
                    for move in moves:
                        self.process_client.move(move)
                self.process_client.turn()
                sleep(0.5)


        return player.is_alive                  # for testing


if __name__ == '__main__':
    Runner().run()
