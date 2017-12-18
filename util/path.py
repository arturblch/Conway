import networkx as nx
from heapq import heappush, heappop
from itertools import count


class AStar:
    def __init__(self, weight='length'):
        self._cost = self.cost
        self._heuristic = self.heuristic
        self._finished = self.finished
        self._build_path = self.build_path
        self._successors = self.successors
        self._weight = weight

    def cost(self, w):
        return w.get(self._weight, 1)

    @staticmethod
    def heuristic(u, v):
        return 0

    @staticmethod
    def finished(u, v):
        return u == v

    @staticmethod
    def build_path(explored, target, node):
        path = [target]
        node = node
        while node is not None:
            path.append(node)
            node = explored[node]
        path.reverse()
        return path

    @staticmethod
    def successors(graph, node):
        return graph[node].items()

    def find_path(self, graph, source, target):
        if source == target:
            return [source, target]
        c = count()
        queue = [(0, next(c), source, 0, None)]
        enqueued = {}
        explored = {}
        while queue:
            _, __, curnode, dist, parent = heappop(queue)
            if self._finished(curnode, target):
                return self._build_path(explored, curnode, parent)
            if curnode in explored:
                continue
            explored[curnode] = parent
            for neighbor, w in self._successors(graph, curnode):
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


class LRAStar(AStar):
    def __init__(self, occupied_nodes, weight='length'):
        super().__init__(weight)
        self._successors = self.successors
        self._occupied_nodes = occupied_nodes

    def successors(self, graph, node):
        result = []
        for node, weight in super().successors(graph, node):
            if node not in self._occupied_nodes:
                result.append((node, weight))
        return result

    def find_path(self, graph, source, target):
        # path = self._find_path(graph, source, target)
        path = super().find_path(graph, source, target)
        next_node = path[1]
        self._occupied_nodes.remove(source)
        self._occupied_nodes.append(next_node)
        return path


if __name__ == '__main__':
    Graph = nx.Graph()
    Graph.add_nodes_from(range(1, 16))
    he = [(i, i + 1) for i in range(1, 16) if i % 5 != 0]
    ve = [(i, i + 5) for i in range(1, 11)]
    Graph.add_edges_from(he + ve)
    # print(Graph.nodes)
    # print(Graph.edges)

    trains = [[1, 15],     # [start, goal]
              [5, 11],
              [15, 5],
              [12, 4]]
    solver = LRAStar([train[0] for train in trains])
    print('T1: {} T2: {} T3: {} T4: {}'.format(*[train[0] for train in trains]))
    while any(map(lambda t: t[0] != t[1], trains)):
        for train in trains:
            train[0] = solver.find_path(Graph, train[0], train[1])[1]
        print('T1: {} T2: {} T3: {} T4: {}'.format(*[train[0] for train in trains]))
