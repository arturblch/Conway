from model.UpObject import UpObject
from itertools import cycle
from model import Move
from util.path import LRAStar


class Strategy:
    def __init__(self, player, map_graph, objects):
        self.player = player
        self.map = map_graph
        self.objects = objects

        for train in self.objects.trains:
            train.point = self.map.get_train_point(train)

        self.solver = LRAStar(train.point for train in self.objects.trains)
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
        town = self.player.town
        trains_armor = 0
        for train_id in self.player.trains:
            if self.objects.trains[train_id].point == town.idx and self.objects.trains[train_id].post_type == 3:
                trains_armor += self.objects.trains[train_id].goods

        sum_armor = town.armor + trains_armor
        train_up = []
        town_up = []

        if sum_armor - town.next_level_price > 40:
            sum_armor -= town.next_level_price
            town_up.append(town.id)

        for train_id in self.player.trains:
            if self.objects.trains[train_id].point == town.idx:
                if sum_armor - self.objects.trains[train_id].next_level_price > 40:
                    sum_armor -= self.objects.trains[train_id].next_level_price
                    train_up.append(train_id)
        if town_up or train_up:
            self.up_ready = True
            self.up_object.update(town_up, train_up)

    def get_moves(self):
        moves = []
        for train_id, points in self.trains_points.items():
            if not points:
                self._get_target_points(self.objects.trains[train_id])

        for train_id, points in self.trains_points.items():
            next_target = self.trains_points[train_id][0]
            if next_target == self.objects.trains[train_id].point:
                self.trains_points[train_id].pop(0)
                if not self.trains_points[train_id]:
                    self._get_target_points(self.objects.trains[train_id])
                next_target = self.trains_points[train_id][0]

            next_step = self.solver.find_path(self.map.Graph,  )

            move_obj = self._move_to_point(self, self.objects.trains[train_id],
                                           next_target)
            if move_obj:
                moves.append()

        if moves:
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
            print('out')
            self.trains_points[train.idx] = [self.player.home]



    def _move_to_point(self, train, arrival_point):
        if train.point is None:
            line = self.map.lines[train.line_idx]
        else:
            line = self.map.Graph.edges(train.point, arrival_point)
            if line is None:
                return None
        need_pos = 0 if line.start_point == arrival_point else line.length 

        if need_pos > train.position:
            speed = 1
        elif need_pos < train.position:
            speed = -1
        else:
            speed = 0

        if line == train.line_idx and speed == train.speed:
            return None
        return Move(line.idx, speed, train.idx)
