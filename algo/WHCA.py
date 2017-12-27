from .PathSolver import PathSolver


class WHCA(PathSolver):
    def __init__(self,
                window,
                rejoin_limit,
                predictor,
                obstacle_penalty,
                obstacle_threshold):

        super().__init__(rejoin_limit, predictor, obstacle_penalty, obstacle_threshold)

        self.window_ = window

        self.make_rejoin_search_ = None
        self.heuristic_map_ = None
        self.nodes_primary_ = 0
        self.nodes_heuristic_ = 0


    def make_rejoin_search(self, from_, to, world, agent):
        return rejoin_search(from_, to, world, self.should_stop_,
                            manhattan_distance_heuristic(to),
                            predicted_cost(self.predctor_.get(), world.tick(), self.obstacle_penalty_),
                            passable_if_not_predicted_obstacle(
                                    self.predctor_.get(),
                                    passable_if_not_reserved(self.agent_reservations_, agent, from_),
                                    self.predictor_ if self.obstacle_threshold_ else 1.0))






