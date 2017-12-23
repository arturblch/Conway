from model.UpObject import UpObject
from itertools import cycle
from model.Move import Move
from algo.PathFinder import WHCAStar
from model.TrafficController import TrafficController


class Strategy:
    def __init__(self, player, map_graph, objects):
        self.player = player
        self.map = map_graph
        self.objects = objects

        for train in self.objects.trains.values():
            train.point = self.map.get_train_point(train)

        self.solver = WHCAStar(self.map.Graph, [train.point for train in self.objects.trains.values()])
        self.up_ready = False
        self.up_object = UpObject()  # Empty up object

        self.trains_roles = self._get_roles()
        self.trains_points = {train_idx : [] for train_idx in self.player.trains}
        self.trains_path = {train_idx : [] for train_idx in self.player.trains}

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
        town = self.player.town

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

        trains_targets = {}

        for train_id, points in self.trains_points.items():

            train = self.objects.trains[train_id]
            if train.point is None:
                print("train %d at line, no find_path" % train_id)
                line = self.map.lines[train.line_idx]
                # if train.speed == -1:
                #     moving_trains.append((train.position, line.start_point, line.end_point))
                # else:
                #     moving_trains.append((line.length - train.position, line.end_point, line.start_point))
                # continue

            next_target = self.trains_points[train_id][0]
            if next_target == self.objects.trains[train_id].point:
                self.trains_points[train_id].pop(0)
                if not self.trains_points[train_id]:
                    self._get_target_points(self.objects.trains[train_id])
                next_target = self.trains_points[train_id][0]

            trains_targets[train_id] = (self.objects.trains[train_id].point, next_target)

        self.solver = TrafficController()
        paths = self.solver.find_paths(self.map, self.objects.trains, trains_targets)

        for train_id in paths:
            path = paths[train_id]
            next_step = path[1]
            print("move %d, %d" % (self.objects.trains[train_id].point, next_step))
            move_obj = self._move_to_point(self.objects.trains[train_id], next_step)
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
                elif (need_cap - post_goods) / need_cap <=0.6:
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
            line = self.map.Graph.get_edge_data(train.point, arrival_point)['line']
            if line is None:
                return None
        speed = -1 if line.start_point == arrival_point else 1

        if line == train.line_idx and speed == train.speed:
            return None
        return Move(line.idx, speed, train.idx)
