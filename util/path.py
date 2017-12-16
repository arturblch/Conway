import networkx as nx
from heapq import heappush, heappop
from itertools import count


Graph = nx.Graph()
Graph.add_nodes_from(range(1, 16))
h = [(i, i + 1) for i in range(1, 16) if i % 5 != 0]
v = [(i, i + 5) for i in range(1, 11)]
Graph.add_edges_from(h + v)
# print(Graph.nodes)
# print(Graph.edges)


def distance(u, v):
    return 0


def finished(u, v):
    return u == v


def successors(node):
    return list(Graph.neighbors(node))


def cost(u, v):
    return 1


def build_path(camefrom, start, goal):
    path = [goal]
    node = camefrom[goal]
    while node != start:
        path.append(node)
        node = camefrom[node]
    path.append(start)
    path.reverse()
    return path


def astar(start, goal):
    closed = []
    open = [start]
    g = {start: 0}
    f = [(distance(start, goal), start)]
    camefrom = {}

    while f:
        _, current = heappop(f)
        if current in closed:
            continue
        if finished(current, goal):
            return build_path(camefrom, start, goal)
        open.remove(current)
        closed.append(current)
        for neighbor in successors(current):
            if neighbor in closed:
                continue
            if current in g.keys():
                d = g[current] + cost(current, neighbor)
            else:
                d = 10000
            if neighbor not in open:
                open.append(neighbor)
            elif d >= g[neighbor]:
                continue
            camefrom[neighbor] = current
            g[neighbor] = d
            heappush(f, (distance(neighbor, goal), neighbor))
    return ':('


print(astar(1, 15))
