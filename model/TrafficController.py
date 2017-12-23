from algo.PathFinder import LRAStar, CAStar, HCAStar, WHCAStar


class TrafficController:
    def __init__(self, algorithm=WHCAStar):
        self.algorithm = algorithm

    def find_paths(self, map_graph, trains, trains_targets):
        graph = map_graph.graph
        occupied_nodes = []
        moving_trains = []
        for train in trains:
            if train.point:
                occupied_nodes.append(train.point)
            else:
                line = map_graph.lines[train.line_idx]
                if train.speed == -1:
                    moving_trains.append((train.position, line.start_point, line.end_point))
                else:
                    moving_trains.append((line.length - train.position, line.end_point, line.start_point))
        solver = self.algorithm(graph, occupied_nodes, moving_trains)
        agents = [(train_id, trains[train_id].point, trains_targets[train_id])
                  for train_id in trains_targets if trains[train_id].point]
        return solver.solve(agents, moving_trains)
