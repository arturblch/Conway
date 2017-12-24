from algo.PathFinder import LRAStar, CAStar, HCAStar, WHCAStar


class TrafficController:
    def __init__(self, algorithm=WHCAStar):
        self.algorithm = algorithm
        self.occupied_lines = None
        self.occupied_nodes = None

    def find_paths(self, map_graph, trains, trains_targets):
        graph = map_graph.Graph
        self.occupied_lines = {i: set() for i in range(5)}
        self.occupied_nodes = {i: set() for i in range(5)}
        moving_trains = {}
        for train in trains.values():
            if train.point:
                self.occupied_nodes[0].add(train.point)
            else:
                line = map_graph.lines[train.line_idx]
                if train.speed == -1:
                    if train.idx in trains_targets:
                        moving_trains[train.idx] = (train.position, trains_targets[train.idx][1], line.end_point, line.start_point)
                    self._occupie_line(train.position, (line.start_point, line.end_point))
                    self.occupied_nodes[train.position].add(line.start_point)
                else:
                    if train.idx in trains_targets:
                        moving_trains[train.idx] = (line.length - train.position, trains_targets[train.idx][1], line.start_point, line.end_point)
                    self._occupie_line(line.length - train.position, (line.end_point, line.start_point))
                    self.occupied_nodes[line.length - train.position].add(line.end_point)
        solver = self.algorithm(graph, self.occupied_nodes, self.occupied_lines)
        agents = {train_id: trains_targets[train_id]
                  for train_id in trains_targets if trains[train_id].point}
        print(self.occupied_nodes)
        print(self.occupied_lines)
        return solver.solve(agents, moving_trains)

    def _occupie_line(self, time, line_points):
        for t in range(time+1):
            self.occupied_lines[t].add(line_points)
