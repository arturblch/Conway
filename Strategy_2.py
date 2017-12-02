from model.Move import Move

class Strategy:
    def __init__(self, player, map_graph, objects):
        self.player = player
        self.map = map_graph
        self.objects = objects
        self.in_progress = True

    def get_moves(self):
        moves = []
        for train_id in self.player.trains:
            train = self.objects.trains[train_id]
            move = self.get_move(train)
            if move:
                moves.append(move)
        return moves

    def get_move(self, train):
        if train.position == 10:
            return Move(1, -1, 0)  # Just test
        elif train.position == 0:
            return Move(1, 1, 0)  # Just test
            
