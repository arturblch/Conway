class Line:
    def __init__(self, idx, length, point):
        self.idx = idx
        self.length = length
        self.start_point = point[0]
        self.end_point = point[1]

    def __repr__(self):
        return f"Line {self.idx}"
