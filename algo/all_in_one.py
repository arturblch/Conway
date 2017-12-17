
def children(point,grid):
    x,y = point.point
    links = [grid[d[0]][d[1]] for d in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]]
    return [link for link in links if link.value != '%']

def manhattan(pos,pos2):
    return abs(pos.x - pos2.x) + abs(pos.y-pos2.y)

def aStar(start, goal, grid):

    current = start
    openset.add(current)

    while openset:
        current = min(openset, key=lambda o:o.G + o.H)
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings
        for node in children(current,grid):
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')

#########################################################################

class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class direction(Enum):
    north = 0,
    east = 1
    south = 2
    west = 3

    all_directions = [
        direction.north,
        direction.east,
        direction.south,
        direction.west
    ]

def translate(p, d):
    if d is direction.north:
        return [p.x, p.y - 1]
    elif d is direction.east:
        return [p.x + 1, p.y]
    elif d is direction.south:
        return [p.x, p.y + 1]
    elif d is direction.west:
        return [p.x - 1, p.y]
    raise ValueError("Unreachable")
    return None

def in_bounds(pos, map_):
    return (p.x >= 0 and
            p.y >= 0 and
            p.x < map_.width() and
            p.y < map_.height())

class Node:
    def __init__(self, value, pos, h, g, steps_distance):
        self.value = value
        self.pos = pos
        self.steps_distance = steps_distance
        self.H = h
        self.G = g
        self.come_from = None

    def f(self):
        return self.G + self.H

    def compare(self, other):
        return self.f() > other.f()


########################################################################

class position_distance_storage:
    def __init__(self):
        self.storage = dict()                # position : Node

    def store(self, pos, node):
        self.storage.update({pos, node})

    def get(self):
        return self.storage

########################################################################

class position_successors:
    def get(self, pos, world):
        result = []

        for d in direction.all_directions:
            n = translate(pos, d)
            if in_bounds(n, world.map) and world.get(n) != title.wall:
                result.append(n)

########################################################################
class reservation_table_record:
    def __init__(self, pos, agent):
        self.pos_ = pos
        self.agent_ = agent

class passable_if_not_reserved:
    def __init__(reserv_table, agent, from_):
        self.reservations_ = reserv_table # position_time : reservation_table_record
        self.agent_ = agent
        self.from_ = from_

    def __call__(where, from_ world, distance):
        if (self.reservations_.count(position_time(where, world.tick() + distance))):
            return False
        vocated = reservations_.find(position_time(from_, world.tick() + distance))

        if (vocated != reservations_.end() and
            vocated.second.from_ and
            vocated.second.from_ == where):
            return False
        return world.get(where) == title.free or !neighbours(where, self.from_)


class passable_if_not_predicted_obstacle:
    def __init__(self, predictor, passable_if_not_reserved, threshold):
        self.predictor_ = predictor
        self.not_reserved_ = passable_if_not_reserved
        self.threshold_ = threshold

    def __call__(self, where, from_, world, distance):
        return (self.not_reserved_(where, from_, world, distance) and
                (!self.predictor_ or
                 self.predictor_.predict_obstacle((where, world.tick() + distance)))
                  <= threshold_)



##############################################################################



class a_star():
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

    def  find_distance(p, world):
        shortest_paths = distance_storage_.get()

        it = shortest_paths.find(p)
        if it != shortest_paths.end():
            return it.second.g
        else:
            return 9999

    def do_find_path(self, world, goal, limit=9999):

        result = []
        current = self.expand_until(goal, world, limit)
        if !current:
            return None
        while current:
            result.append(current.pos)
            current = current.come_from

        return result

    def expand_until(self, end, world, limit=9999):
        while not len(self.heap_):
            if self.stop_flag_:
                return None

            current = self.heap_.top()
            current_coord = Cordinate(current.pos, current.steps_distance)

            assert self.open_.count(current_coord)
            assert !self.closed_.count(current_coord)

            self.heap_.pop()
            self.open_.erase(current_coord)

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
                        neighbor_handle.g  = current.g + step_cost
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



####################################################################################################




















def next_move(pacman, food, grid):
    #Convert all the points to instances of Node
    for x in xrange(len(grid)):
        for y in xrange(len(grid[x])):
            grid[x][y] = Node(grid[x][y],(x,y))
    #Get the path
    path = aStar(grid[pacman[0]][pacman[1]],grid[food[0]][food[1]], grid)
    #Output the path
    print len(path) - 1
    for node in path:
        x, y = node.point
        print x, y




pacman_x, pacman_y = [ int(i) for i in raw_input().strip().split() ]
food_x, food_y = [ int(i) for i in raw_input().strip().split() ]
x,y = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, x):
    grid.append(list(raw_input().strip()))

next_move((pacman_x, pacman_y),(food_x, food_y), grid)


