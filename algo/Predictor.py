from world import direction_to, in_bounds, translate, position, tail, directtion
from enum import IntEnum

from collections import OrderedDict


class movement(IntEnum):
    north = 0
    east = 1
    south = 2
    west = 3
    stay = 4

    num_moves = 5


def directed_to_movement(direct):
    return movement(int(direct))


class movement_estimator():
    def __init__(self, world):

        self.store_positions(world)

        self.last_tick_ = 0
        self.last_obstacles_ = OrderedDict()  # obstacle_id : position
        self.move_count_ = [0, 0, 0, 0, 0]
        self.estimate_ = [0.0, 0.0, 0.0, 0.0, 1.0]
        self.num_moves_ = 0

    def store_positions(self, world):
        if self.last_tick_ == 0:
            self.last_tick_ = world.tick()
        else:
            assert world.tick() == self.last_tick_ + 1
            self.last_obstacles_.clear()
            for pos, obstacle in world.obstacles().items():
                self.last_obstacles_.update({obstacle.id(): pos})

    def update(self, world):
        for pos, obstacle in world.obstacles().items():
            _id = obstacle.id()
            last = self.last_obstacles_[_id]

            if last == next(reversed(self.last_obstacles_)):
                continue

            curent = pos

            if curent == last.second:
                self.move_count_[movement.stay] += 1
            else:
                self.move_count_[directed_to_movement(
                    direction_to(last.second, curent))] += 1
            self.num_moves_ += 1

        self.store_positions(world)

        if (self.num_moves_ > 0):
            for move in range(int(movement.stay) + 1):
                self.estimate_[move] = self.move_count_[move] / self.num_moves_

        def estimate(self, move):
            return self.estimate_[int(move)]


def estimates_diff(self, x, y):
    result = 0.0

    for i in range(len(x)):
        result += abs(x[i] - y[i])

    return result


class predictor:
    def update_obstacles(world):
        raise NotImplementedError("Use update_obstacles from parent")

    def predict_obstacle(self, ):
        raise NotImplementedError("Use update_obstacles from parent")

    def field(self, ):
        raise NotImplementedError("Use update_obstacles from parent")


class matrix_predictor(predictor):
    def __init__(self, world, cutoff=0):
        self.estimator_ = movement_estimator(world)
        self.last_estimate_ = self.estimator_.estimates()
        self.transition_ = self.make_transition_matrix(world, self.estimator_)
        self.states_ = []
        self.last_update_time_ = 0
        self.width_ = 0
        self.cutoff_ = cutoff

    def linear(self, pos):
        return pos.y * self.width_ + pos.x

    def update_obstacles(self, world):
        if self.last_update_time_ == world.tick():
            return

        self.estimator_.update(world)
        self.states_.clear()
        if (estimates_diff(self.estimator_.estimates(), self.last_estimate_) >
                0.01 and self.last_update_time_ % 5 == 0):
            self.transition_ = self.make_transition_matrix(
                world, self.estimator_)
            self.last_estimate_ = self.estimator_.estimates()

        known_state = obstacle_state(
            world.map().width() * world.map().height())

        known_state.fill(0.0)

        for pos_obstacle in world.obstacles():
            known_state(self.linear(pos_obstacle.first)) = 1.0
        self.states_.append(known_state)
        self.last_update_time_ = world.tick()

    def predict_obstacle(self, pos_time):
        if (self.cutoff_
                and pos_time.time - self.last_update_time_ > self.cutoff_):
            pos_time.time = self.last_update_time_ + self.cutoff_

        while pos_time - self.last_update_time_ >= len(self.states_):
            self.states_.append(self.transition_ * self.states_[-1])

        return self.states_[pos_time - self.last_update_time_](self.linear(
            pos_time.x, pos_time.y))

    def field(self, result):
        result = dict()

        for t in range(len(self.states_)):
            for i in range(len(self.states_[t])):
                result[i % self.width_, i / self.width_,
                       self.last_update_time_] = self.states_[t](i)

        return result

    def make_transition_matrix(self, world, estimator):
        m = world.map()
        map_size = m.width() * m.height()

        transitions = []
        result = []

        for from_y in range(m.height()):
            for from_x in range(m.width()):
                from_ = position(from_x, from_y)
                if world.get(from_) == tail.wall or world.get(
                        from_) == tail.agent:
                    continue

                neibours = []

                for direct in directtion:
                    to = translate(from_, direct)
                    if not in_bounds(to, m) or world.get(to) == tail.wall:
                        continue

                    neibours.append(to)

                stay_probability = estimator.estimate(movement.stay)
                leftover = 1.0 - stay_probability

                if not neibours:
                    transitions.append((self.linear(from_), self.linear(from_),
                                        1.0))
                    continue

                for pos in neibours:
                    transition_probability = estimator.estimate(
                        directed_to_movement(int(direction_to(from_, to))))

                    transitions.append((self.linear(to), self.linear(from_),
                                        transition_probability))

                    leftover -= transition_probability

                transitions.append((self.linear(from_), self.linear(from_),
                                    transition_probability))

            result.extend(
                transitions)  # Нужно дописать матрицу и заполнение в нее

        return result


class predicted_cost:
    def __init__(self, predictor, start_tick, obstacle_penalty):
        self.predictor_ = predictor
        self.start_tick_ = start_tick
        self.obstacle_penalty_ = obstacle_penalty

    def __call__(self, from_, to):
        if not self.predictor_ or from_.position() == to.position:
            return 1.0
        return (1.0 + self.predictor_.predict_obstacle(
            to.x, to.y, self.start_tick_ + to.time) * self.obstacle_penalty_)


def make_matrix(self, world, cutoff):
    return matrix_predictor(world, cutoff)
