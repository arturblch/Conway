class A_star:
    def __init__(self, from_, to, passable, distance, step_cost, stop_flag):
        self.from_ = from_
        self.to_ = to
        self.heap_ = None
        self.expanded_ = 0
        self.node_pool_ = None
        self.open_ = None
        self.closed_ = None
        self.distance_storage_ = None
        self.passable_ = passable
        self.distance_ = distance
        self.step_cost_ = step_cost
        self.stop_flag_ = stop_flag


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
            return None
        while current:
            result.append(current.pos)
            current = current.come_from

        return result

    def expand_until(self, end, world, limit=9999):
        while not len(self.heap_):
            if self.stop_flag_:
                return None

            current = self.heap_.pop(0)
            current_coord = Cordinate(current.pos, current.steps_distance)

            assert self.open_.count(current_coord)
            assert !self.closed_.count(current_coord)

            self.heap_.pop()
            self.open_.pop(current_coord)

            if (ShouldClosePred.get(current_coord)):
                self.closed_.insert({current_coord})

            self.distance_storage_.store(current.pos, current)

            self.expanded_ += 1

            if (current.steps_distance == limit):
                return None

            neighbours = SuccesorsFunc.get(current.pos, world)

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

