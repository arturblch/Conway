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
        self._occupied_lines = {0: []}

    def successors(self, source, time):
        result = []
        for node, weight in super().successors(source, time):
            delta = self._cost(weight)
            if time+delta not in self._occupied_nodes.keys():
                self._occupied_nodes[time+delta] = []
            if time+1 not in self._occupied_lines.keys():
                self._occupied_lines[time+1] = []
            if node not in self._occupied_nodes[time+delta]\
                    and (source, node) not in self._occupied_lines[time+1]:
                result.append((node, weight))
        return result

    def replan(self, source, target):
        plan = super().find_path(source, target)
        time = 0
        prev_node = plan[0]
        for node in plan[1:]:
            if prev_node == node:
                continue
            delta = self._cost(self._graph[prev_node][node])
            for t in range(time, time + delta + 1):
                if t not in self._occupied_lines.keys():
                    self._occupied_lines[t] = [(node, prev_node), ]
                else:
                    self._occupied_lines[t].append((node, prev_node))
            if time + delta not in self._occupied_nodes.keys():
                self._occupied_nodes[time + delta] = [node, ]
            else:
                self._occupied_nodes[time + delta].append(node)
            time = time + delta
            prev_node = node
        return plan

    def solve(self, agents, moving_trains):
        plans = []
        for delta, target, source in moving_trains:
            if delta not in self._occupied_nodes.keys():
                self._occupied_nodes[delta] = [target, ]
            else:
                self._occupied_nodes[delta].append(target)
            for t in range(delta + 1):
                if t not in self._occupied_lines.keys():
                    self._occupied_lines[t] = [(target, source), ]
                else:
                    self._occupied_lines[t].append((target, source))
        for agent in agents:
            plans.append(self.replan(*agent))
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
                    heappush(queue, (ncost + h, next(c), neighbor, ncost, curnode))
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
    def __init__(self, graph, occupied_nodes, window=50, weight='length'):
        super().__init__(graph, occupied_nodes, weight)
        self._finished = self.finished
        self.window = window

    def finished(self, u, v, t):
        return u == v or t >= self.window
