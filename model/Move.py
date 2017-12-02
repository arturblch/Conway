class Move:
    def __init__(self, line_idx, speed, train_idx):
        self.line_idx = line_idx
        self.speed = speed
        self.train_idx = train_idx

    def __repr__(self):
        return 'line - %d, speed - %d, train -%d' %(
                self.line_idx, self.speed, self.train_idx)