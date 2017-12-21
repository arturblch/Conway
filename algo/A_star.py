class A_star:
    def __init__(self, from_, to, passable, finished, distance, step_cost):
        self.from_ = from_
        self.to_ = to
        self.heap_ = []
        self.expanded_ = 0
        self.node_pool_ = None
        self.open_ = None
        self.closed_ = None
        self.distance_storage_ = dict()  # pos : node
        self.passable_ = passable
        self.distance_ = distance
        self.step_cost_ = step_cost
        self._finished = finished

        start = node(from_, 0.0, distance_(from_), 0 )
        self.heap_.append(start)


    def find_path(self, world, window):
        goal = lambda n : n.steps_distance == window
        return do_find_path(world, goal)

    def find_distance(p, world):
        shortest_paths = distance_storage_.get()

        it = shortest_paths.find(p)
        if it != shortest_paths.end():
            return it.second.g
        else:
            return 9999

    def do_find_path(self, world, goal, limit=9999):

        result = []
        current = self.expand_until(goal, world, limit)
        if not current:
            return []
        while current:
            result.append(current.pos)
            current = current.come_from

        return result.reverse()

    def expand_until(self, end, world, limit=9999):
        while not len(self.heap_):
            if self.stop_flag_:
                return None

            current = min(self.heap_, key = lambda x: x.f())
            current_coord = Cordinate(current.pos, current.steps_distance)

            assert(self.open_.count(current_coord))
            assert(!self.closed_.count(current_coord)

            self.heap_.pop(current)
            self.open_.pop(current_coord)

            self.closed_.insert({current_coord})

            self.distance_storage_.store(current.pos, current)

            self.expanded_ += 1

            if (current.steps_distance == limit):
                return None

            neighbours = self.successors(current.pos)

            if Cordinate(current.pos, current.steps_distance +1) != current_coord:
                neighbours.append(current.pos)


            for neighbor in neighbours:
                neighbor_coord = Cordinate(neighbor, current.steps_distance +1)

                if self.closed_.count(neighbor_coord):
                    continue

                if (!self.passable_(neighbor, current.pos, world, current.steps_distance + 1)):
                    continue

                step_cost = self.step_cost_(current_coord, neighbor_coord, current.steps_distance + 1)

                n = self.open_.find(neighbor_coord)
                if n != self.open.end():
                    neighbor_handle = n.second
                    if neighbor_handle.g > current.g + step_cost:
                        neighbor_handle.g = current.g + step_cost
                        neighbor_handle.come_from = current
                        neighbor_handle.steps_distance = current.steps_distance + 1
                        self.heap_.decrease(neighbor_handle)

                    else:
                        neighbor_node = self.node_pool_.construct(Node(neghbour, current.g + step_cost,
                                                                        self.distance_(neighbor, world),
                                                                        current.steps_distance + 1))
                        handh = self.push(neighbor_node)
                        neighbor_node.come_from = current
                        self.open_.insert((neighbor_node, h))
            if end(current):
                return current

        return None

class node:
    def __init__(pos, g, h, steps_distance):
        self.pos = pos
        self.g = g
        self.h = h
        self.steps_distance = steps_distance

    def f(self):
        return g + h

    def __gt__(self, other):
        return self.f() > other.f()
