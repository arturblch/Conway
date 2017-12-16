import networkx as nx
from heapq import heappush, heappop
from itertools import count


Graph = nx.Graph()
Graph.add_nodes_from(range(1, 16))
he = [(i, i + 1) for i in range(1, 16) if i % 5 != 0]
ve = [(i, i + 5) for i in range(1, 11)]
Graph.add_edges_from(he + ve)
# print(Graph.nodes)
# print(Graph.edges)


def finished(u, v):
    return u == v


def build_path(explored, target, node):
    path = [target]
    node = node
    while node is not None:
        path.append(node)
        node = explored[node]
    path.reverse()
    return path


def successors(graph, node):
    return graph[node].items()


def successors_lra(graph, node, initial):
    result = []
    for node, weight in successors(graph, node):
        if node not in occupied_nodes:
            result.append((node, weight))
    return result


def cost(w, weight):
    return w.get(weight, 1)


def heuristic(u, v):
    return 0


def astar(graph, source, target, weight='length'):
    c = count()
    queue = [(0, next(c), source, 0, None)]
    enqueued = {}
    explored = {}
    while queue:
        _, __, curnode, dist, parent = heappop(queue)
        if finished(curnode, target):
            return build_path(explored, curnode, parent)
        if curnode in explored:
            continue
        explored[curnode] = parent
        for neighbor, w in successors_lra(graph, curnode, source):
            if neighbor in explored:
                continue
            ncost = dist + cost(w, weight)
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            else:
                h = heuristic(neighbor, target)
            enqueued[neighbor] = ncost, h
            heappush(queue, (ncost + h, next(c), neighbor, ncost, curnode))
    return ':('


t1 = [1, 15]   # start, goal
t2 = [5, 11]
occupied_nodes = [t1[0], t2[0]]
while (t1[0] != t1[1]) or (t2[0] != t2[1]):
    print(f'T1: {t1[0]} T2: {t2[0]}')
    t1[0] = astar(Graph, t1[0], t1[1])[1]
    occupied_nodes[0] = t1[0]
    t2[0] = astar(Graph, t2[0], t2[1])[1]
    occupied_nodes[1] = t2[0]
print(f'T1: {t1[0]} T2: {t2[0]}')
occupied_nodes = []
