import networkx as nx
from algo.PathFinder import LRAStar, CAStar, HCAStar, WHCAStar


def test_LRAStar():
    print('LRA*')
    graph = get_graph()
    trains = get_state()
    solver = LRAStar(graph, [train[0] for train in trains.values()])
    print('T1: {} T2: {} T3: {} T4: {}'.format(*[trains[train_id][0] for train_id in trains]))
    while any(map(lambda t: t[0] != t[1], trains.values())):
        for train_id in trains:
            trains[train_id][0] = solver.solve(trains[train_id][0], trains[train_id][1])[1]
        print('T1: {} T2: {} T3: {} T4: {}'.format(*[trains[train_id][0] for train_id in trains]))
    assert all(map(lambda t: t[0] == t[1], trains.values()))


def test_CAStar():
    print('CA*')
    graph = get_graph()
    trains = get_state()
    solver = CAStar(graph, [train[0] for train in trains.values()])
    paths = solver.solve(trains, [])
    for train_id in paths:
        path = paths[train_id]
        print(f'T{train_id}: ', path)
        assert trains[train_id][-1] == path[-1]


def test_HCAStar():
    print('HCA*')
    graph = get_graph()
    trains = get_state()
    solver = HCAStar(graph, [train[0] for train in trains.values()])
    paths = solver.solve(trains, [])
    for train_id in paths:
        path = paths[train_id]
        print(f'T{train_id}: ', path)
        assert trains[train_id][-1] == path[-1]


def test_WHCAStar():
    print('WHCA*')
    graph = get_graph()
    trains = get_state()
    solver = WHCAStar(graph, [train[0] for train in trains.values()], window=10)
    paths = solver.solve(trains, [])
    for train_id in paths:
        path = paths[train_id]
        print(f'T{train_id}: ', path)


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
    state = {1: [1, 15],  # [start, goal]
             2: [5, 11],
             3: [15, 5],
             4: [12, 4]}
    return state
