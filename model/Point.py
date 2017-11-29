class Point:
    def __init__(self, idx, post_id):
        self.idx = idx
        self.post_id = post_id

    def __repr__(self):
        return f"Point {self.idx}"
