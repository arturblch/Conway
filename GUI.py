import pygame as pg
from pygame.locals import *
import math
from pprint import pprint

BACKGROUND_IMAGE = 'grass.jpg'
POINT_LABEL_COLOR = (255, 255, 255)
LINE_COLOR = (101, 67, 33)
RADIUS = 20

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
green_2 = (20, 230, 20)
blue = (0, 0, 255)
blue_2 = (20, 20, 230)
yelow = (255, 255, 0)
black = (0, 0, 0)
grey = (128, 128, 128)

player_colors = [red, green_2, blue_2, yelow]

class GUI:
    def __init__(self,
                 player,
                 map_graph,
                 objects,
                 strategy,
                 width=600,
                 height=600):
        pg.init()
        self.width = width
        self.height = height
        self.display_width = self.width - 2 * RADIUS
        self.display_height = self.height - 2 * RADIUS

        self.player = player
        self.map = map_graph
        self.objects = objects
        self.strategy = strategy
        self.screen = pg.display.set_mode((self.width, self.height + 100))
        self.surf = pg.Surface((width, height))
        self.stat = pg.Surface((width, 100))
        self.background = pg.image.load(BACKGROUND_IMAGE).convert_alpha()
        self.background = pg.transform.scale(self.background, (width, height))
        self.clock = pg.time.Clock()
        self.fps = 30
        self.paused = True
        self.onestep = False
        pg.display.set_caption("Train Game")
        self.myfont = pg.font.SysFont('arial', 15)
        self.player_colors = dict()

    def draw_points(self, ):
        for point in self.map.points:
            x_pos = int((self.display_width * self.map.pos[point][0] + RADIUS))
            y_pos = int(
                (self.display_height * self.map.pos[point][1] + RADIUS))

            pg.draw.circle(self.surf, black, (x_pos, y_pos), RADIUS)

        for post_id, idx in self.map.posts.items():
            x_pos = int((self.display_width * self.map.pos[idx][0] + RADIUS))
            y_pos = int((self.display_height * self.map.pos[idx][1] + RADIUS))

            if post_id in self.objects.markets.keys():
                mask = pg.Surface((RADIUS * 2, RADIUS * 2))
                mask.fill(green)
                mask.set_alpha(128)
                self.surf.blit(mask, (x_pos - RADIUS, y_pos - RADIUS))
                pg.draw.circle(self.surf, green, (x_pos, y_pos), RADIUS)

            if post_id in self.objects.storages.keys():
                mask = pg.Surface((RADIUS * 2, RADIUS * 2))
                mask.fill(red)
                mask.set_alpha(128)
                self.surf.blit(mask, (x_pos - RADIUS, y_pos - RADIUS))
                pg.draw.circle(self.surf, green, (x_pos, y_pos), RADIUS)

            if post_id in self.objects.towns.keys():
                mask = pg.Surface((RADIUS * 2, RADIUS * 2))
                mask.fill(blue)
                mask.set_alpha(128)
                self.surf.blit(mask, (x_pos - RADIUS, y_pos - RADIUS))
                pg.draw.circle(self.surf, blue, (x_pos, y_pos), RADIUS)
                # s.set_alpha(128)

    def draw_edges(self, edgelist=None):
        if edgelist is None:
            edgelist = self.map.lines

        for l in edgelist.values():

            pg.draw.line(
                self.surf, LINE_COLOR,
                (int((self.display_width) * self.map.pos[l.start_point][0] +
                     RADIUS),
                 int((self.display_width) * self.map.pos[l.start_point][1] +
                     RADIUS)),
                (int((self.display_height) * self.map.pos[l.end_point][0] +
                     RADIUS),
                 int((self.display_height) * self.map.pos[l.end_point][1] +
                     RADIUS)), 5)

    def draw_node_labels(self):
        for idx in self.map.points:
            num_idx = pg.font.Font(None, 25).render(str(idx), False, white)
            text_pos_x = int((self.display_width) * self.map.pos[idx][0] +
                             RADIUS - (num_idx.get_width() / 2))
            text_pos_y = int((self.display_height) * self.map.pos[idx][1] +
                             RADIUS - (num_idx.get_height() / 2))
            self.surf.blit(num_idx, (text_pos_x, text_pos_y))

        for post_id, idx in self.map.posts.items():
            text_pos_x = int((self.display_width) * self.map.pos[idx][0] +
                             RADIUS - (num_idx.get_width() / 2))
            text_pos_y = int((self.display_height) * self.map.pos[idx][1] +
                             RADIUS - (num_idx.get_height() / 2))
            name = ""
            product = ""
            population = ""
            if post_id in self.objects.markets.keys():
                name = self.objects.markets[post_id].name
                product = self.objects.markets[post_id].product
            elif post_id in self.objects.storages.keys():
                name = self.objects.storages[post_id].name
                product = self.objects.storages[post_id].armor
            else:
                name = self.objects.towns[post_id].name
                product = self.objects.towns[post_id].product
                armor = self.objects.towns[post_id].armor
                population = self.objects.towns[post_id].population

                post_population = pg.font.Font(None, 19).render(
                    str(population), False, white)
                self.surf.blit(post_population,
                               (text_pos_x - RADIUS, text_pos_y - RADIUS))
                post_armor = pg.font.Font(None, 19).render(
                    str(armor), False, white)
                self.surf.blit(post_armor,
                               (text_pos_x + RADIUS, text_pos_y - RADIUS - 10))

            post_name = pg.font.Font(None, 19).render(name, False, white)
            post_product = pg.font.Font(None, 19).render(
                str(product), False, white)

            self.surf.blit(post_name, (text_pos_x, text_pos_y - RADIUS))
            self.surf.blit(post_product, (text_pos_x, text_pos_y + RADIUS))

    def draw_fps_score_tick(self):
        self.stat.blit(
            pg.font.Font(None, 30).render(
                str('fps : %.1f' % self.clock.get_fps()), False,
                (255, 255, 255)), (20, 20))
        self.stat.blit(
            pg.font.Font(None, 30).render(
                str('score : %d' % self.objects.get_score()), False,
                (255, 255, 255)), (200, 20))
        self.stat.blit(
            pg.font.Font(None, 30).render(
                str('tick : %d' % self.objects.tick), False, (255, 255, 255)),
            (400, 20))

    def draw_train(self):
        for train in self.objects.trains.values():
            if train.player_id not in self.player_colors.keys():
                self.player_colors[train.player_id] = player_colors.pop(0)
            color = self.player_colors[train.player_id]
            if train.line_idx == None:
                continue
            line = self.map.lines[train.line_idx]

            (x1, y1) = self.map.pos[line.start_point]
            (x2, y2) = self.map.pos[line.end_point]
            train_pos = train.position / line.length
            (x, y) = (x2 * train_pos + x1 * (1.0 - train_pos),
                      y2 * train_pos + y1 * (1.0 - train_pos))

            if train.speed == 1:
                angle = math.atan2(y1 - y2, x2 - x1) / (
                    2.0 * math.pi) * 360  # degrees
            elif train.speed == -1:
                angle = math.atan2(y2 - y1, x1 - x2) / (
                    2.0 * math.pi) * 360  # degrees
            else:
                angle = None

            train_surf = pg.Surface((20, 20), pg.SRCALPHA)
            center = (int(train_surf.get_width() / 2), int(
                train_surf.get_height() / 2))
            pg.draw.circle(train_surf, color, center, 10)
            if angle != None:
                pg.draw.polygon(train_surf, black, [[0, 0], [20, 10], [0, 20]],
                                0)
                train_surf = pg.transform.rotate(train_surf, angle)
            self.surf.blit(train_surf,
                           (int(self.display_width * x + center[0]),
                            int(self.display_height * y + center[1])))

    def update(self):
        self.surf.blit(self.background, (0, 0))
        self.stat.fill(grey)
        self.draw_edges()
        self.draw_points()
        self.draw_fps_score_tick()
        self.draw_node_labels()
        self.draw_train()

        self.screen.blit(self.surf, (0, 0))
        self.screen.blit(self.stat, (0, self.height))

        pg.display.update()

    def turn(self):
        if self.player.is_alive == True:
            self.onestep = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.player.is_alive = False
                    return
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        self.player.is_alive = False
                        return
                    elif event.key == K_n:
                        self.onestep = True
                    elif event.key == K_p:
                        self.paused = not self.paused
                    elif event.key == K_r:
                        pprint(self.strategy.trains_points)
                        pprint(self.strategy.paths)

                    elif (event.key == K_PLUS) or (event.key == K_EQUALS):
                        self.fps += 1
                    elif event.key == K_MINUS:
                        self.fps -= 1
                        if self.fps < 1: self.fps = 1

            self.update()
            pg.display.flip()
            self.clock.tick(self.fps)

    def update_objects(self, objects):
        self.objects = objects

    def close(self):
        pg.quit()


if __name__ == '__main__':
    gui = GUI()
    gui.run()
