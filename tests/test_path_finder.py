import networkx as nx

from algo.PathFinder import LRAStar, CAStar, HCAStar, WHCAStar


def test_LRAStar():
    print('LRA*')
    graph = get_graph()
    trains = get_state()
    solver = LRAStar(graph, [train[0] for train in trains])
    print('T1: {} T2: {} T3: {} T4: {}'.format(*[train[0] for train in trains]))
    while any(map(lambda t: t[0] != t[1], trains)):
        for train in trains:
            train[0] = solver.solve(train[0], train[1])[1]
        print('T1: {} T2: {} T3: {} T4: {}'.format(*[train[0] for train in trains]))
    assert all(map(lambda t: t[0] == t[1], trains))


def test_CAStar():
    print('CA*')
    graph = get_graph()
    trains = get_state()
    solver = CAStar(graph, [train[0] for train in trains])
    for i, path in enumerate(solver.solve(trains, [])):
        print(f'T{i+1}: ', path)
        assert trains[i][1] == path[-1]


def test_HCAStar():
    print('HCA*')
    graph = get_graph()
    trains = get_state()
    solver = HCAStar(graph, [train[0] for train in trains])
    for i, path in enumerate(solver.solve(trains, [])):
        print(f'T{i+1}: ', path)
        assert trains[i][1] == path[-1]


def test_WHCAStar():
    print('WHCA*')
    graph = get_graph()
    trains = get_state()
    solver = WHCAStar(graph, [train[0] for train in trains], window=10)
    for i, path in enumerate(solver.solve(trains, [])):
        print(f'T{i+1}: ', path)


def get_graph():
    graph = nx.Graph()
    graph.add_nodes_from(range(1, 16))
    he = [(i, i + 1) for i in range(1, 16) if i % 5 != 0]
    ve = [(i, i + 5) for i in range(1, 11)]
    graph.add_edges_from(he + ve)
    # print(Graph.nodes)
    # print(Graph.edges)
    return graph


def get_state():
    state = [[1, 15],  # [start, goal]
             [5, 11],
             [15, 5],
             [12, 4]]
    return state
