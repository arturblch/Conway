import networkx as nx
from heapq import heappush, heappop
from itertools import count
import copy


class AStar:
    """
    Implementation of A* algorithm.

    AStar.solve(source, target) return a list of nodes in a shortest path between source and target
    """

    def __init__(self, graph, weight='length'):
        self._cost = self.cost
        self._heuristic = self.heuristic
        self._finished = self.finished
        self._build_path = self.build_path
        self._successors = self.successors
        self._weight = weight
        self._graph = graph

    def cost(self, w):
        return w.get(self._weight, 1)

    def heuristic(self, u, v):
        return 0

    def finished(self, u, v, time):
        return u == v

    @staticmethod
    def build_path(explored, target, node):
        path = [target]
        while node is not None:
            path.append(node)
            node = explored[node]
        path.reverse()
        return path

    def successors(self, node, time):
        return self._graph[node].items()

    def find_path(self, source, target):
        if source == target:
            return [source, target]
        c = count()
        queue = [(0, next(c), source, 0, None)]
        enqueued = {}
        explored = {}
        while queue:
            _, time, curnode, dist, parent = heappop(queue)
            if self._finished(curnode, target, time):
                return self._build_path(explored, curnode, parent)
            if curnode in explored:
                continue
            explored[curnode] = parent
            for neighbor, w in self._successors(curnode, time):
                if neighbor in explored:
                    continue
                ncost = dist + self._cost(w)
                if neighbor in enqueued:
                    qcost, h = enqueued[neighbor]
                    if qcost <= ncost:
                        continue
                else:
                    h = self._heuristic(neighbor, target)
                enqueued[neighbor] = ncost, h
                heappush(queue, (ncost + h, next(c), neighbor, ncost, curnode))
        return [source, source]

    def solve(self, source, target):
        return self.find_path(source, target)


class LRAStar(AStar):
    """
    Implementation of Local-Repair A* algorithm.

    LRAStar.solve(source, target) return a list of nodes in a shortest path between source and target
    """

    def __init__(self, graph, occupied_nodes, weight='length'):
        super().__init__(graph, weight)
        self._successors = self.successors
        self._occupied_nodes = occupied_nodes

    def successors(self, node, time):
        result = []
        for node, weight in super().successors(node, time):
            if node not in self._occupied_nodes:
                result.append((node, weight))
        return result

    def find_path(self, source, target):
        path = super().find_path(source, target)
        next_node = path[1]
        if source in self._occupied_nodes:
            self._occupied_nodes.remove(source)
        self._occupied_nodes.append(next_node)
        return path

    def solve(self, source, target):
        return self.find_path(source, target)


class CAStar(AStar):
    """
    Implementation of Cooperative A* algorithm.

    LRAStar.solve(agents) return a list of paths for each agent. Each agent defined by source
    and target nodes. Ex: LRAStar.solve([[start1, target1], [start2, target2], ...])

    !!!Arrived agents are ignored!!!
    """

    def __init__(self, graph, occupied_nodes, weight='length'):
        super().__init__(graph, weight)
        self._successors = self.successors
        self._occupied_nodes = {0: occupied_nodes}

    def successors(self, node, time):
        result = []
        for node, weight in super().successors(node, time):
            if time + 1 not in self._occupied_nodes.keys():
                self._occupied_nodes[time + 1] = []
            if node not in self._occupied_nodes[time + 1]:
                result.append((node, weight))
        return result

    def replan(self, source, target):
        plan = super().find_path(source, target)
        for i, node in enumerate(plan):
            self._occupied_nodes[i].append(node)
        return plan

    def solve(self, train_target):
        plans = dict()
        for train, target in train_target.items():
            plans.update({train: self.replan(train.point, target)})
        return plans


class RRAStar(AStar):
    """
    Reverse Resumable A*

    Secondary algorithm for HCA*.
    Using as distance function in HCA*.
    """

    def find_path(self, source, target):
        if source == target:
            return 0
        c = count()
        queue = [(0, next(c), source, 0, None)]
        enqueued = {}
        explored = {}

        def RRA(position):
            while position not in explored:
                _, time, curnode, dist, parent = heappop(queue)
                if self._finished(curnode, position, time):
                    break
                if curnode in explored:
                    continue
                explored[curnode] = parent
                for neighbor, w in self._successors(curnode, time):
                    if neighbor in explored:
                        continue
                    ncost = dist + self._cost(w)
                    if neighbor in enqueued:
                        qcost, h = enqueued[neighbor]
                        if qcost <= ncost:
                            continue
                    else:
                        h = self._heuristic(neighbor, source)
                    enqueued[neighbor] = ncost, h
                    heappush(queue,
                             (ncost + h, next(c), neighbor, ncost, curnode))
            return enqueued[position]

        return RRA(target)[0]


class HCAStar(CAStar):
    """
    Hierarchical Cooperative A* algorithm.

    HCAStar.solve(agents) return a list of paths for each agent. Each agent defined by source
    and target nodes. Ex: HCAStar.solve([[start1, target1], [start2, target2], ...])

    !!!Arrived agents are ignored!!!
    """

    def __init__(self, graph, occupied_nodes, weight='length'):
        super().__init__(graph, occupied_nodes, weight)
        self._heuristic = self.heuristic

    def heuristic(self, u, v):
        slv = RRAStar(self._graph)
        return slv.find_path(u, v)


class WHCAStar(HCAStar):
    """
    Windowed Hierarchical Cooperative A* algorithm.

    WHCAStar.solve(agents) return a list of paths for each agent. Each agent defined by source
    and target nodes. Ex: WHCAStar.solve([[start1, target1], [start2, target2], ...])

    !!!Arrived agents are ignored!!!    ???
    """

    def __init__(self, graph, occupied_nodes, window=10, weight='length'):
        super().__init__(graph, occupied_nodes, weight)
        self._finished = self.finished
        self.window = window

    def finished(self, u, v, t):
        return u == v or t >= self.window


class Position:
    def __init__(self, point, line, pos):
        self.point = point
        self.line = line
        self.pos = pos


class PathSolver(AStar):
    """
    Implementation of CA
    """

    def __init__(self, map_graph, reserv_pos, invalid_field, weight='length'):
        super().__init__(map_graph.Graph, weight)
        self.map = map_graph  # need lines property for func get_neighbors
        self._successors = self.successors
        self._reserv_pos = reserv_pos
        self._invalid_field = invalid_field

    def successors(self, pos, time):
        result = []
        neighbours = self.map.get_neighbors_pos(pos)

        result = [neighbour for neighbour in neighbours
                  if self.passable(pos, neighbour)]

        return result

    def passable(self, from_pos, to_pos, time):
        if time + 1 not in self._reserv_pos.keys():
            self._reserv_pos[time + 1] = []

        if (to_pos in self._reserv_pos[time + 1]
                or to_pos in self._reserv_pos[time]
                and from_pos in self._reserv_pos[time + 1]):
            return False
        elif to_pos in self._invalid_field:
            return False

        return True


def test_LRAStar(state):
    print('LRA*')
    trains = copy.deepcopy(state)
    solver = LRAStar(Graph, [train[0] for train in trains])
    print(
        'T1: {} T2: {} T3: {} T4: {}'.format(*[train[0] for train in trains]))
    while any(map(lambda t: t[0] != t[1], trains)):
        for train in trains:
            train[0] = solver.solve(train[0], train[1])[1]
        print('T1: {} T2: {} T3: {} T4: {}'.format(
            *[train[0] for train in trains]))


def test_CAStar(state):
    print('CA*')
    trains = copy.deepcopy(state)
    solver = CAStar(Graph, [train[0] for train in trains])
    for i, path in enumerate(solver.solve(trains)):
        print(f'T{i+1}: ', path)


def test_HCAStar(state):
    print('HCA*')
    trains = copy.deepcopy(state)
    solver = HCAStar(Graph, [train[0] for train in trains])
    for i, path in enumerate(solver.solve(trains)):
        print(f'T{i+1}: ', path)


def test_WHCAStar(state):
    print('WHCA*')
    trains = copy.deepcopy(state)
    solver = WHCAStar(Graph, [train[0] for train in trains], window=10)
    for i, path in enumerate(solver.solve(trains)):
        print(f'T{i+1}: ', path)


if __name__ == '__main__':
    Graph = nx.Graph()
    Graph.add_nodes_from(range(1, 16))
    he = [(i, i + 1) for i in range(1, 16) if i % 5 != 0]
    ve = [(i, i + 5) for i in range(1, 11)]
    Graph.add_edges_from(he + ve)
    # print(Graph.nodes)
    # print(Graph.edges)

    state = [
        [1, 15],  # [start, goal]
        [5, 11],
        [15, 5],
        [12, 4]
    ]

    test_LRAStar(state)
    test_CAStar(state)
    test_HCAStar(state)
    test_WHCAStar(state)
