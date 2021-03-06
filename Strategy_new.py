from model.UpObject import UpObject
from itertools import cycle
from model.Move import Move
from model.Map import Position
from algo.WCA import WCAStar
import logging
from pprint import pprint, pformat
from model.TrafficController import TrafficController

from random import shuffle

# create logger
logger = logging.getLogger('Strategy')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('Reservation.log', mode='w')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class Strategy:
    def __init__(self, player, map_graph, objects):
        self.player = player
        self.map = map_graph
        self.objects = objects

        self.paths = dict()

        for train in self.objects.trains.values():
            train.point = self.map.get_train_point(train)

        self.up_ready = False
        self.up_object = UpObject()  # Empty up object

        self.trains_reservations = {}  # train_id : {time, pos}
        self.trains_roles = self._get_roles()
        self.trains_points = {
            train.idx: []
            for train in self.objects.get_my_trains(player.idx)
        }
        self.trains_path = {train_idx: [] for train_idx in self.player.trains}

        self.pos_markets = {
            Position(m.point)
            for m in self.objects.markets.values()
        }
        self.pos_storages = {
            Position(s.point)
            for s in self.objects.storages.values()
        }

    def get_enemy_trains_fields(self):
        enemy_trains = self.objects.get_enemy_trains(self.player.idx)
        enemy_trains_pos = [
            Position(t.point, t.line_idx, t.position) for t in enemy_trains
        ]
        enemy_trains_fields = []
        for pos in enemy_trains_pos:
            enemy_trains_fields.extend(self.map.get_neighbors_pos(pos))
            enemy_trains_fields.append(pos)

        return set(enemy_trains_fields)

    def get_my_trains_pos(self, t_id):
        my_trains = self.objects.get_my_trains(self.player.idx)
        return {
            t.idx: Position(t.point, t.line_idx, t.position)
            for t in my_trains
        }

    def get_invalid_posts_pos(self, train):
        if train.goods == 0:
            if self.trains_roles[train.idx] == 2:
                return self.pos_storages
            if self.trains_roles[train.idx] == 3:
                return self.pos_markets
        else:
            return set()

    def get_towns_pos(self):
        return {Position(town.point) for town in self.objects.towns.values()}

    def valid(self, train, from_pos, next_pos):
        towns_pos = self.get_towns_pos()
        invalid_posts = self.get_invalid_posts_pos(train)
        enemy_field = self.get_enemy_trains_fields()
        my_trains_pos = self.get_my_trains_pos(train.idx)

        invalid = invalid_posts.union(enemy_field)
        if next_pos is None:
            return False
        for train_id, reserv_path in self.trains_reservations.items():
            if train_id == train.idx:
                continue
            if self.objects.tick + 1 not in reserv_path.keys():
                if next_pos == my_trains_pos[train_id]:
                    print('other train next, without reservation')
                    return False
                else:
                    continue

            elif (next_pos == reserv_path[self.objects.tick + 1]
                  and next_pos not in towns_pos
                  or next_pos == reserv_path[self.objects.tick]
                  and from_pos == reserv_path[self.objects.tick + 1]):
                print('next pos in reservation, or next_pos in colision')
                return False
        return True

    def _get_roles(self):
        roles = {}
        rol_gen = cycle([2, 3])
        for train in self.objects.get_my_trains(self.player.idx):
            roles[train.idx] = next(rol_gen)
        return roles

    def get_upgrade(self):
        self._get_up_object()
        if self.up_ready:
            self.up_ready = False
            return self.up_object

    def _get_up_object(self):
        home = self.player.home
        town = self.player.town

        armor = town.armor
        train_up = []
        town_up = []

        if town.level == 1:

            if armor - town.next_level_price > 40:
                armor -= town.next_level_price
                town_up.append(town.idx)
        else:
            if armor - town.next_level_price > 40:
                armor -= town.next_level_price
                town_up.append(town.idx)
            for train in self.objects.get_my_trains(self.player.idx):
                if self.objects.trains[train.idx].point == town.point:
                    if armor - self.objects.trains[train.
                                                   idx].next_level_price > 40:
                        armor -= self.objects.trains[
                            train.idx].next_level_price
                        train_up.append(train.idx)
        if town_up or train_up:
            self.up_ready = True
            self.up_object.update(town_up, train_up)

    def update_targets(self):
        self.change_targets()
        for train_id, points in self.trains_points.items():
            # if empty (stay at town) get new
            train = self.objects.trains[train_id]
            if len(points) == 0:
                self._get_target_points(train)

            if self.trains_points[train_id][0] == train.point:
                self.trains_points[train_id].pop(0)

            if len(points) == 0:
                self._get_target_points(train)

    def get_moves(self):
        self.update_targets()

        moves = []
        trains_targets = dict()
        for train_id in self.trains_points:
            train = self.objects.trains[train_id]
            if train.point:
                trains_targets[train.idx] = (train.point, self.trains_points[train.idx][0])
        print(trains_targets)

        self.solver = TrafficController()
        paths = self.solver.find_paths(self.map, self.objects.trains, trains_targets)

        for train_id in paths:
            path = paths[train_id]
            if path:
                next_step = path[1]
                print("move {}, {}".format(self.objects.trains[train_id].point, next_step))
                move_obj = self._move_to_point(self.objects.trains[train_id], next_step)
                moves.append(move_obj)
            else:
                train = self.objects.trains[train_id]
                moves.append(Move(train.line_idx, 0, train.idx))

        # moves = self.step()
        # print(move_obj)
        if moves:
            return moves

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

    def _get_target_points(self, train):
        town = self.objects.towns[self.player.home]
        if self.trains_roles[train.idx] == 2:
            post_list = [(self.map.get_distance(town.point, post.point), post)
                         for post in self.objects.markets.values()]
        elif self.trains_roles[train.idx] == 3:
            post_list = [(self.map.get_distance(town.point, post.point), post)
                         for post in self.objects.storages.values()]
        post_list = sorted(
            [dist_post for dist_post in post_list], key=lambda x: x[0])
        if train.point == town.point and train.goods == 0:
            need_cap = train.goods_capacity
            path = []
            for dist_post in post_list:
                post = dist_post[1]
                if self.trains_roles[train.idx] == 2:
                    post_goods = post.product_capacity
                elif self.trains_roles[train.idx] == 3:
                    post_goods = post.armor_capacity
                if need_cap - post_goods> 20:
                    path.append(self.map.posts[post.idx])
                    need_cap -= post_goods
                elif need_cap - post_goods <= 20:
                    path.append(self.map.posts[post.idx])
                    break
            path.append(town.point)
            self.trains_points[train.idx] = path
        else:
            print("train - ", train.idx, " has - ", train.goods, " goods")
            self.trains_points[train.idx] = [town.point]

    def change_targets(self):
        town = self.objects.towns[self.player.home]
        need_cap = 45 * max(town.population, (
            town.product_capacity - town.product) / town.product_capacity * 5)

        cur_cap = sum([
            train.goods_capacity
            for train in self.objects.get_my_trains(self.player.idx)
            if self.trains_roles[train.idx] == 2
        ])

        if cur_cap < need_cap:
            self.add_role(2)
        elif cur_cap - need_cap > 45:
            self.add_role(3)

    def add_role(self, role):
        town = self.objects.towns[self.player.home]
        trains_home = [
            train for train in self.objects.get_my_trains(self.player.idx)
            if train.point == town.point and self.trains_roles != role
        ]
        if trains_home:
            self.trains_roles[trains_home[0].idx] = role
            self._get_target_points(trains_home[0])

    def step(self):
        moves = []
        trains = dict()
        trains_order = []
        self.update_targets()

        for train in self.objects.get_my_trains(self.player.idx):
            pos = Position(train.point, train.line_idx, train.position)
            trains.update({train.idx: pos})
            trains_order.append(train.idx)
        shuffle(trains_order)

        while len(trains_order):
            train_id = trains_order.pop(0)
            train = self.objects.trains[train_id]
            maybe_next = self.next_step(train_id)
            pos = trains[train_id]

            if not maybe_next:
                print("No Path")
                for t in trains_order:
                    self.unreserve(t)
                    self.paths[t] = []

            if not self.valid(train, pos, maybe_next):
                print("Path Invalid")
                self.paths[train_id] = []
                maybe_next = self.next_step(train_id)

            if not maybe_next:
                maybe_next = pos

            line_speed = self.pos_to_line_speed(pos, maybe_next)
            if line_speed[0] == train.line_idx and line_speed[1] == train.speed:
                continue
            if train.speed == -line_speed[1]:
                moves.append(Move(line_speed[0], 0, train_id))
            moves.append(Move(line_speed[0], line_speed[1], train_id))
        logger.info("reservation on tick - %d \n %s", self.objects.tick,
                    pformat(self.trains_reservations, indent=4))
        pprint(self.trains_roles)
        return moves

    def next_step(self, train_id):
        train = self.objects.trains[train_id]
        train_pos = Position(train.point, train.line_idx, train.position)

        if train_id not in self.paths.keys():
            self.paths[train_id] = []
        if (len(self.paths[train_id]) < 2
                or self.paths[train_id][0] != train_pos):
            self.paths[train_id] = self.recalculate(train_id)

        if (len(self.paths[train_id]) < 2):
            return None

        assert (self.paths[train_id][0] == train_pos)
        self.paths[train_id].pop(0)
        return self.paths[train_id][0]

    def recalculate(self, train_id):

        self.unreserve(train_id)

        target_pos = Position(self.trains_points[train_id][0])
        new_path = self.find_path(train_id, target_pos)

        if new_path:
            self.reserve(train_id, new_path, self.objects.tick)
        else:
            print("Found no path for ", train_id)

        return new_path

    def unreserve(self, train_id):
        if train_id in self.trains_reservations.keys():
            self.trains_reservations.pop(train_id)

    def reserve(self, train_id, path, time_offset):
        self.trains_reservations[train_id] = dict()
        for time in range(len(path)):
            pos = path[time]

            self.trains_reservations[train_id].update({
                time + time_offset: pos
            })

    def find_path(self, train_id, target):
        train = self.objects.trains[train_id]
        source = Position(train.point, train.line_idx, train.position)

        invalid_pos = self.get_invalid_posts_pos(train).union(
                self.get_enemy_trains_fields())
        towns = self.get_towns_pos()
        trains_pos = self.get_my_trains_pos(train_id)
        a_star = WCAStar(self.map, towns, trains_pos, self.trains_reservations,
                         invalid_pos, source, target, self.objects.tick, 10)
        new_path = a_star.find_path()
        return new_path

    def pos_to_line_speed(self, from_, to):
        if from_ == to:
            line = from_.line
            speed = 0
        else:
            if from_.point != None:
                line = to.line
                line_obj = self.map.lines[line]
                from_pos = line_obj.length if from_.point == line_obj.end_point else 0
            else:
                from_pos = from_.pos
                line = from_.line

            speed = -1 if from_pos > to.pos else 1

        return (line, speed)
