from model.Move import Move

class Strategy:
    def __init__(self, player, map_graph, objects):
        self.player = player
        self.map = map_graph
        self.objects = objects
        self.in_progress = True

    def get_moves(self):
        moves = []
        move = self.get_move()
        moves.append(move)
        return moves

    def get_move(self):
        return Move(1, 1, 0)  # Just test
