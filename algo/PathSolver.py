from random import shuffle

def solved(world):
    for pos, agent in world.agents().items():
        if pos != agent.target:
            return False

    return True

def is_waiting_at_goal(agent, path):
    return path[0] == agent.target and path[-1] == agent.target


class Solver:
    def __init__(self):
        self.should_stop_ = False

    def step():
        pass

    def name():
        pass

    def stat_names():
        pass

    def stat_values():
        pass

    def get_path():
        pass

    def get_obstacle_field():
        pass

    def window():
        pass

    def kill():
        self.should_stop_ = True

######################################################################################


class PathSolver(Solver):
    def __init__(self, rejoin_limit=0, predictor, obstacle_penalty=100, obstacle_threshold=0.1):
        super.__init__(self)
        self.rejoin_limit_ = rejoin_limit
        self.predictor_ = predictor
        self.obstacle_penalty_ = obstacle_penalty
        self.obstacle_threshold_ = obstacle_threshold

        self.times_without_path_ = 0
        self.recalculations_ = 0
        self.path_invalid_ = 0
        self.nodes_rejoin_ = 0
        self.rejoin_attempts_ = 0
        self.rejoin_successes_ = 0

        self.paths_ = dict()  # agent_id : path


    def stat_names(self):
        return ["Path not found", "Recalculations", "Path invalid",
          "Rejoin nodes expanded", "Rejoin attempts", "Rejoin successes",
          "Rejoin success rate"]

    def stat_values(self):
        return [self.times_without_path_,
                self.recalculations_,
                self.path_invalid_,
                self.nodes_rejoin_,
                self.rejoin_attempts_,
                self.rejoin_successes_]


    def on_path_invalid(self, agent_id):
        raise NotImplementedError("Use on_path_invalid from parent")

    def on_path_found(self, agent_id, path, world):
        raise NotImplementedError("Use on_path_found from parent")

    def path_valid(path, world):
        raise NotImplementedError("Use path_valid from parent")

    def find_path(pos, world):
        raise NotImplementedError("Use find_path from parent")


    def step(self, world):
        self.should_stop_ = False

        if self.predictor_:
            self.predictor_.update_obstacles(world)

        agents = []
        agent_order = []
        finished_agents = []

        for pos, agent in world.agents().items():
            agents.update({agent.id() : pos})
            agent_order.append(agent.id())

            if is_waiting_at_goal(agent, self.paths_[agent.id()]):
                finished_agents.append(agent.id())

        shuffle(agent_order)

        need_recalculate = False
        for _id , path in self.paths_.items():
            if len(path) < 2 and not _id in finished_agents:
                need_recalculate = True
                break

        if need_recalculate:
            agent_order.sort(key=lambda x:  x in finished_agents)

            for _id in finished_agents:
                self.paths_[_id] = [] # Тип пути

        for _id in agent_order:
            pos = agents[_id]
            agent = world.get_agent(pos)

            maybe_next = self.next_step(pos, world)

            if not maybe_next:
                if pos != agent.target:
                    print('No path')
                    self.times_without_path_ += 1
                continue

            if pos == maybe_next:
                continue

            if self.should_stop_:
                return None

            direct = direction_to(pos, maybe_next)
            if not valid(action(pos, dir), world):
                print('Path invalid for pos - ', pos)
                self.path_invalid_ += 1

                old_path = self.paths_[agent.id()]
                self.paths_[agent.id()] = []
                maybe_next = next_step(pos, world, old_path)
            if not maybe_next or pos == maybe_next:
                continue

            if self.should_stop_:
                return None

            direct = direction_to(pos, maybe_next)
            act = action(pos, direct)
            world = apply(act, world)



    def next_step(self, from_, world, rand_eng, old_path):
        agent = world.get_agent(from_)

        if (len(self.paths_[agent.id()]) < 2):
            self.paths_[agent.id()] = self.recalculate()

        if (len(self.paths_[agent.id()]) < 2):
            return

        self.paths_[agent.id()].pop()
        return self.paths_[agent.id()].back()


    def recalculate(self, from_, world, agent_id, rand_eng, old_path):
        self.on_path_invalid(agent_id)

        if self.rejoin_limit_ > 0 and old_path:
            self.rejoin_attempts_ += 1

            p = self.rejoin_path(from_, world, old_path)
            if (p):
                if self.path_valid(p, world):
                    self.rejoin_successes_ += 1
                    new_path = p

        if self.should_stop_:
            return

        if not len(new_path):
            self.recalculations_ += 1
            new_path = self.find_path(from_, world, rand_eng)

        if len(new_path):
            self.on_path_found(agent_id, new_path, world)

        return new_path

    def rejoin_path(from_, world, old_path):
        if not len(old_path):
            return
        to = None
        target_positions = dict()
        point = old_path.rbegin()
        while point != old_path.rend():
            if world.get(point) == title.free:
                if not to:
                    to = point
                target_positions.update(point, point)
        if not to:
            return
        agent = world.get_agent(from_)

        as_ = self.make_rejoin_search(from_, to, world, agent)
        goal = lambda p : return target_positions.count(p)
        join_path = as_.find_path(world, goal, self.rejoin_limit_)

        self.nodes_rejoin_ += as_.nodes_expanded()
        if not len(join_path or self.should_stop_):
            return
        rejoin_point = target_positions[join_path.front()]

        result = dict()

        old_end = rejoin_point.base() - 1
        new_begin = join_path.begin()

        result.update(result.end(), old_path.begin(), old_end)
        result.update(result.end(), new_begin, join_path.end())

        return result