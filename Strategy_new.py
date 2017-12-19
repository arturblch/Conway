from model.UpObject import UpObject
from itertools import cycle
from model.Move import Move
from model.Map import Position
from util.path import CAStar


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
        return [Position(t.point, t.line_idx, t.position) for t in enemy_trains]

    def valid(self, train, next_pos):
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
            if not points:
                self._get_target_points(self.objects.trains[train_id])

    def get_moves(self):
        moves = []

        self.update_targets()

        states = dict()

        for train_id, points in self.trains_points.items():

            if self.objects.trains[train_id].point == None:
                print("train %d at line, no find_path" % train_id)
                continue

            next_target = self.trains_points[train_id][0]
            if next_target == self.objects.trains[train_id].point:
                self.trains_points[train_id].pop(0)
                if not self.trains_points[train_id]:
                    self._get_target_points(self.objects.trains[train_id])
                next_target = self.trains_points[train_id][0]
            states.update({self.objects.trains[train_id]: next_target})

        next_steps = self.solver.solve(states)

        for train, path in next_steps.items():
            move_obj = self._move_to_point(train, path[1])
            print("train %d at point, next_step %d" % (train.idx, path[1]))

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

                old_path = self.paths.pop(train_id)
                maybe_next = self.next_step(pos, old_path)
            if not maybe_next:
                continue

            line_speed = self.pos_to_move(pos, maybe_next)

            if line_speed[0] == train.line_idx and line_speed[1] == train.speed:
                continue
            moves.append(Move(line_speed[0], line_speed[1], train_id))

        return moves

    def pos_to_move(self, from_, to):
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
