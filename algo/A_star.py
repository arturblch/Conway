class position_distance_storage:
    def __init__(self):
        self.storage = dict()

    def store(self, pos, node):
        self.storage.update({pos: node})

    def get(self):
        return self.storage


class space_time_coordinate:
    def __init__(self, time, pos):
        self.time = time
        self.pos = pos

    def __eq__(self, other):
        return self.time == other.time and self.pos == other.pos

    def __hash__(self):
        if self.pos.point != None:
            return hash((self.time, self.pos.point, None, None))
        else:
            return hash((self.time, None, self.pos.line, self.pos.pos))

    def __repr__(self):
        return "time - %d " % self.time + str(self.pos)

class A_star:
    def __init__(self, map_graph, from_, to, cur_tick, window):
        self.map = map_graph
        self.from_ = from_
        self.to = to
        self.open_ = dict()  # time_pos : node
        self.closed_ = dict()  # time_pos : node
        self.expanded_ = 0
        self.distance_storage_ = position_distance_storage()
        self.cur_tick = cur_tick
        self.window = window

        start = node(from_, 0.0, self.distance(from_), 0)
        self.open_[space_time_coordinate(0, from_)] = start

    # always true for base implementation
    def passable(self, from_, to_, time):
        return True

    def finished(self, node):
        return node.pos == self.to or node.time == self.window

    # unitary step cost
    def step_cost(self, from_, to):
        return 1

    # base successors func
    def successors(self, pos):
        return self.map.get_neighbors_pos(pos)

    # manhatan distance to goal(to)
    def distance(self, pos):
        if pos.point != None:
            return self.map.get_distance(pos.point, self.to.point)
        else:
            return self.map.get_distance_from_line(pos.line, pos.pos,
                                                   self.to.point)

    # func for hierarchial_distance
    def find_distance(self, p, world):
        shortest_paths = self.distance_storage_.get()

        it = shortest_paths.find(p)
        if it != shortest_paths.end():
            return it.second.g
        else:
            return 9999

    def find_path(self):

        result = []
        current = self.expand_loop()
        if not current:
            return []
        while current:
            result.append(current.pos)
            current = current.come_from

        result.reverse()
        return result

    def expand_loop(self, limit=100):
        while len(self.open_):
            current = min(self.open_.values(), key=lambda x: x.f())
            current_coord = space_time_coordinate(current.steps_distance,
                                                  current.pos)

            assert current_coord in self.open_, str(current_coord.time) + str(current_coord.pos)
            assert (current_coord not in self.closed_)

            if self.finished(current_coord):
                return current

            self.open_.pop(current_coord)
            self.closed_[current_coord] = current

            self.distance_storage_.store(current.pos, current)
            self.expanded_ += 1

            if (current.steps_distance == limit):
                return None

            neighbours = self.successors(current.pos)
            if not space_time_coordinate(
                   current.steps_distance + 1,  current.pos) == current_coord:
                neighbours.append(current.pos)

            for neighbor in neighbours:
                neighbour_coord = space_time_coordinate(
                    current.steps_distance + 1, neighbor)
                if neighbour_coord in self.closed_.keys():
                    continue
                if not (self.passable(current.pos, neighbor,
                                      current.steps_distance + self.cur_tick)):
                    continue
                step_cost = self.step_cost(current.pos, neighbor)

                if any(neighbour_coord == coord for coord in self.open_.keys()):
                    n = self.open_[neighbour_coord]
                    if n.g > current.g + step_cost:
                        n.g = current.g + step_cost
                        n.steps_distance = current.steps_distance + 1
                        n.come_from = current
                else:
                    n = node(neighbor, current.g + step_cost,
                             self.distance(neighbor),
                             current.steps_distance + 1)
                    n.come_from = current
                    self.open_[neighbour_coord] = n
        return None


class node:
    def __init__(self, pos, g, h, steps_distance):
        self.pos = pos
        self.g = g
        self.h = h
        self.steps_distance = steps_distance

        self.come_from = None

    def f(self):
        return self.g + self.h

    def __gt__(self, other):
        return self.f() > other.f()
