from model.UpObject import UpObject
from itertools import cycle
from model.Move import Move
from model.Map import Position
from algo.WCA import WCAStar
import logging
from pprint import pprint, pformat

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

        self.up_ready = False
        self.up_object = UpObject()  # Empty up object

        self.trains_reservations = {}  # train_id : {time, pos}
        self.trains_path = {train_idx: [] for train_idx in self.player.trains}

        self.trains_roles = dict()
        self.trains_points = {
            train.idx: []
            for train in self.objects.get_my_trains(player.idx)
        }

    def get_markets_pos(self):
        return {
            Position(market.point)
            for market in self.objects.markets.values()
        }

    def get_storages_pos(self):
        return {
            Position(storage.point)
            for storage in self.objects.storages.values()
        }

    def get_towns_pos(self):
        return {Position(town.point) for town in self.objects.towns.values()}

    def get_enemy_trains_fields(self):
        enemy_trains = self.objects.get_enemy_trains(self.player.idx)
        enemy_trains_pos = [
            Position(train=train) for train in enemy_trains
        ]
        enemy_trains_fields = []
        for pos in enemy_trains_pos:
            enemy_trains_fields.extend(self.map.get_neighbors_pos(pos))
            enemy_trains_fields.append(pos)

        return set(enemy_trains_fields)

    def get_my_trains_pos(self, t_id):
        my_trains = self.objects.get_my_trains(self.player.idx)
        return {
            train.idx: Position(train=train)
            for train in my_trains
        }

    def get_invalid_posts_pos(self, train):
        if train.goods == 0:
            if self.trains_roles[train.idx] == 2:
                return self.get_storages_pos()
            if self.trains_roles[train.idx] == 3:
                return self.get_markets_pos()
        else:
            return set()

    def valid(self, train, from_pos, next_pos):
        towns_pos = self.get_towns_pos()
        invalid_posts = self.get_invalid_posts_pos(train)
        enemy_field = self.get_enemy_trains_fields()
        my_trains_pos = self.get_my_trains_pos(train.idx)

        invalid = invalid_posts.union(enemy_field)
        if next_pos is None:
            return False
        if next_pos in invalid:
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

    def set_roles(self):
        roles = {}
        rol_gen = cycle([2, 3])
        for train in self.objects.get_my_trains(self.player.idx):
            roles[train.idx] = next(rol_gen)
        self.trains_roles = roles

    def get_upgrade(self):
        self._get_up_object()
        if self.up_ready:
            self.up_ready = False
            return self.up_object

    def _get_up_object(self):
        home = self.player.home
        town = self.objects.towns[home]

        armor = town.armor
        train_up = []
        town_up = []

        if town.level == 1:

            if armor - town.next_level_price > 40:
                armor -= town.next_level_price
                town_up.append(town.idx)
        else:
            if town.next_level_price:
                if armor - town.next_level_price > 40:
                    armor -= town.next_level_price
                    town_up.append(town.idx)
            for train in self.objects.get_my_trains(self.player.idx):
                if self.objects.trains[train.idx].point == town.point:
                    if self.objects.trains[train.idx].next_level_price:
                        if armor - self.objects.trains[train.
                                                       idx].next_level_price > 40:
                            armor -= self.objects.trains[
                                train.idx].next_level_price
                            train_up.append(train.idx)
        if town_up or train_up:
            self.up_ready = True
            self.up_object.update(town_up, train_up)

    def update_targets(self):
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
        move_obj = self.step()
        if move_obj:
            return move_obj

    def _get_target_points(self, train):
        town = self.objects.towns[self.player.home]
        if self.trains_roles[train.idx] == 2:
            post_list = self.map.distance_to_all_targets(Position(train=train), self.objects.markets.values())
        elif self.trains_roles[train.idx] == 3:
            post_list = self.map.distance_to_all_targets(Position(train=train), self.objects.storages.values())

        need_cap = train.goods_capacity
        path = []
        for dist_post in post_list:
            post = dist_post[1]
            if self.trains_roles[train.idx] == 2:
                post_goods = post.product_capacity
            elif self.trains_roles[train.idx] == 3:
                post_goods = post.armor_capacity
            if need_cap - post_goods > 20:
                path.append(self.map.posts[post.idx])
                need_cap -= post_goods
            elif need_cap - post_goods <= 20:
                path.append(self.map.posts[post.idx])
                break
        path.append(town.point)
        self.trains_points[train.idx] = path

    def rebalance_of_roles(self):
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
        empty_trains = [
            train for train in self.objects.get_my_trains(self.player.idx)
            if train.goods == 0 and self.trains_roles[train.idx] != role
        ]
        if empty_trains:
            train = empty_trains[0]
            self.trains_roles[train.idx] = role
            self.trains_points[train.idx] = []
            self._get_target_points(train)

    def step(self):
        if not self.trains_roles:
            self.set_roles()

        self.rebalance_of_roles()
        self.update_targets()

        moves = []
        trains_order = sorted([train.idx for  train in self.objects.get_my_trains(self.player.idx)])

        while len(trains_order):
            train_id = trains_order.pop(0)
            train = self.objects.trains[train_id]
            pos = Position(train=train)

            next_pos = self.next_step(train_id)

            if not next_pos:
                print("No Path")
                for t in trains_order:
                    self.unreserve(t)
                    self.paths[t] = []

            if not self.valid(train, pos, next_pos):
                print("Path Invalid")
                self.paths[train_id] = []
                next_pos = self.next_step(train_id)

            if not next_pos:
                next_pos = pos

            line_speed = self.pos_to_line_speed(pos, next_pos)
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
        train_pos = Position(train=train)

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
        source = Position(train=train)

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
