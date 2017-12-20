from model.UpObject import UpObject
from itertools import cycle
from model.Move import Move
from model.Map import Position
from util.path import CAStar, PathSolver


class Strategy:
    def __init__(self, player, map_graph, objects):
        self.player = player
        self.map = map_graph
        self.objects = objects

        self.paths = dict()

        for train in self.objects.trains.values():
            train.point = self.map.get_train_point(train)

        self.solver = CAStar(
            self.map.Graph,
            [train.point for train in self.objects.trains.values()])
        self.trains_reservations = dict()

        self.up_ready = False
        self.up_object = UpObject()  # Empty up object

        self.trains_roles = self._get_roles()
        self.trains_points = {
            train_idx: []
            for train_idx in self.player.trains
        }
        self.trains_path = {train_idx: [] for train_idx in self.player.trains}

        self.pos_markets = [
            Position(m.point) for m in self.objects.markets.values()
        ]
        self.pos_storages = [
            Position(s.point) for s in self.objects.storages.values()
        ]

    def get_enemy_trains_pos(self):
        enemy_trains = self.objects.get_enemys()
        return [
            Position(t.point, t.line_idx, t.position) for t in enemy_trains
        ]

    def get_innvalid_pos(self, train):
        invalid_positions = []

        enemy_pos = self.get_enemy_trains_pos()
        for pos in enemy_pos:
            invalid_positions.extend(self.map.get_neighbors_pos(pos))
            invalid_positions.append(pos)

        if train.goods == 0:
            if self.trains_roles[train.idx] == 2:
                for stor_pos in self.pos_storages:
                    if stor_pos not in invalid_positions:
                        invalid_positions.append(stor_pos)
            if self.trains_roles[train.idx] == 2:
                for market_pos in self.pos_markets:
                    if market_pos not in invalid_positions:
                        invalid_positions.append(market_pos)

    def valid(self, train, next_pos):
        invalid_pos = self.get_innvalid_pos(train)
        return next_pos in invalid_positions

    def _get_roles(self):
        roles = {}
        rol_gen = cycle([2, 3])
        for train_id in self.player.trains:
            roles[train_id] = next(rol_gen)
        return roles

    def get_upgrade(self):
        self._get_up_object()
        if self.up_ready:
            self.up_ready = False
            up = self.up_object
            self.up_object.update([], [])
            return up

    def _get_up_object(self):
        home = self.player.home
        town = self.objects.towns[home]

        armor = town.armor
        train_up = []
        town_up = []

        if armor - town.next_level_price > 40:
            armor -= town.next_level_price
            town_up.append(town.idx)

        for train_id in self.player.trains:
            if self.objects.trains[train_id].point == town.idx:
                if armor - self.objects.trains[train_id].next_level_price > 40:
                    armor -= self.objects.trains[train_id].next_level_price
                    train_up.append(train_id)
        if town_up or train_up:
            self.up_ready = True
            self.up_object.update(town_up, train_up)

    def update_targets(self):
        for train_id, points in self.trains_points.items():
            # if empty (stay at town) get new
            if len(points) == 0:
                self._get_target_points(self.objects.trains[train_id])

            if self.objects.trains[train_id][0] == self.objects.trains[
                    train_id].point:
                self.trains_points[train_id].pop(0)

            if len(points) == 0:
                self._get_target_points(self.objects.trains[train_id])

    def get_moves(self):
        self.update_targets()

        move_obj = self.solver.solve(states)
        if move_obj:
            moves.append(move_obj)

        return moves

    def _get_target_points(self, train):
        if self.trains_roles[train.idx] == 2:
            post_list = sorted(
                self.objects.markets.values(),
                key=lambda x: x.product_capacity)
        elif self.trains_roles[train.idx] == 3:
            post_list = sorted(
                self.objects.storages.values(), key=lambda x: x.armor_capacity)

        if train.point == self.player.home and train.goods == 0:
            need_cap = train.goods_capacity
            path = []
            for post in post_list:
                distance = self.map.get_distance(train.point, post.idx)
                if self.trains_roles[train.idx] == 2:
                    post_goods = min(
                        post.product + post.replenishment * distance,
                        post.product_capacity)
                elif self.trains_roles[train.idx] == 3:
                    post_goods = min(
                        post.armor + post.replenishment * distance,
                        post.armor_capacity)
                if (need_cap - post_goods) / need_cap > 0.6:
                    continue
                elif (need_cap - post_goods) / need_cap <= 0.6:
                    path.append(self.map.posts[post.idx])
                    break
            path.append(self.player.home)
            self.trains_points[train.idx] = path
        else:
            self.trains_points[train.idx] = [self.player.home]

    def _move_to_point(self, train, arrival_point):
        if train.point == arrival_point:
            return None
        if train.point is None:
            line = self.map.lines[train.line_idx]
        else:
            line = self.map.Graph.get_edge_data(train.point,
                                                arrival_point)['line']
            if line is None:
                return None
        speed = -1 if line.start_point == arrival_point else 1

        if line == train.line_idx and speed == train.speed:
            return None
        return Move(line.idx, speed, train.idx)

    def step(self):
        moves = []

        self.update_targets()

        trains = []
        trains_order = []

        for train_id in self.player.trains:
            train = self.objects.trains[train_id]
            pos = Position(train.point, train.line_idx, train.position)
            trains.update({train_id: pos})
            trains_order.append(train_id)

        for train_id in trains_order:
            train = self.objects.trains[train_id]

            maybe_next = self.next_step(train_id)

            pos = trains[train_id]

            if not maybe_next:
                if pos != self.trains_points[train_id][0]:  # not at target
                    print("No Path")
                continue

            if not self.valid(train, maybe_next):
                print("Path Invalid")

                maybe_next = self.next_step(train_id)

            if not maybe_next:
                continue

            line_speed = self.pos_to_line_speed(pos, maybe_next)

            if line_speed[0] == train.line_idx and line_speed[1] == train.speed:
                continue
            moves.append(Move(line_speed[0], line_speed[1], train_id))

        return moves

    def get_invalid_type(self, train):
        if train.goods != 0:
            return 0
        elif self.trains_roles[train.idx] == 2:
            return 3
        else:
            return 2

    def next_step(self, train_id):
        train = self.objects.trains[train_id]
        train_pos = Position(train.point, train.line_idx, train.position)

        if (len(self.paths[train_id]) < 2):
            self.paths[train_id] = self.recalculate(train_id, train_pos)

        if (len(self.paths[train_id]) < 2):
            return None

        assert (self.paths[train_id][0] == train_pos)
        self.paths[train_id].pop(0)
        return self.paths[train_id][0]

    def recalculate(self, train_id, train_pos):

        self.unreserve(train_id)

        target_pos = Position(self.trains_points[train_id][0])
        new_path = self.find_path(train_pos, target_pos, train_id)

        if new_path:
            self.reserve(train_id, new_path)

        return new_path

    def unreserve(self, train_id):
        for time, reserv_pos in self.trains_reservations:
            if train_id in reserv_pos.keys():
                reserv_pos.pop(train_id)

    def reserve(self, train_id, path, time_offset):
        for time in range(len(path)):
            pos = path[time]
            train_id_pos = {train_id: pos}

            assert (
                train_id_pos not in self.trains_reservations[time
                                                             + time_offset])
            if time == 0:
                continue
            else:
                self.trains_reservations.update({time + time_offset: pos})

    def find_path(self, source, target, train_id):
        train = self.objects.trains[train_id]
        invalid_pos = self.get_innvalid_pos(train)
        a_star = PathSolver(
            self.map_graph,
            self.trains_reservations,
            invalid_pos
        )
        new_path = a_star.find_path(source, target)
        return new_path

    def pos_to_line_speed(self, from_, to):
        if from_ == to:
            line = from_.line
            speed = 0
        else:
            if from_.point != None:
                line = to.line
                line_obj = self.objects.lines[line]
                from_pos = line_obj.length if from_.point == line.end_point else 0
            else:
                from_pos = from_.pos

            speed = -1 if from_pos > to.pos else 1

        return (line, speed)
