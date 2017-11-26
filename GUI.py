import pygame as pg
from pygame.locals import *
import numpy
from Runner import Runner
from Strategy import Strategy

BACKGROUND_IMAGE = 'grass.jpg'
POINT_COLOR = (0, 0, 0)
POINT_LABEL_COLOR = (255, 255, 255)
LINE_COLOR = (101, 67, 33)
RADIUS = 20


class GUI:
    def __init__(self, width=600, height=600):
        pg.init()
        self.width = width
        self.height = height
        self.display_width = self.width - 2 * RADIUS
        self.display_height = self.height - 2 * RADIUS
        self.map = None
        self.screen = pg.display.set_mode((self.width, self.height))
        self.surf = pg.Surface((width, height))
        self.background = pg.image.load(BACKGROUND_IMAGE).convert_alpha()
        self.background = pg.transform.scale(self.background, (width, height))
        self.clock = pg.time.Clock()
        self.fps = 60
        pg.display.set_caption("Train Game")
        self.myfont = pg.font.SysFont('arial', 15)

    def draw_points(self, nodelist=None):
        if nodelist is None:
            nodelist = self.map.Graph.nodes()
        for v in nodelist:
            x_pos = int((self.display_width * self.map.pos[v][0] + RADIUS))
            y_pos = int((self.display_height * self.map.pos[v][1] + RADIUS))
            pg.draw.circle(self.surf, POINT_COLOR, (x_pos, y_pos), RADIUS)

    def draw_edges(self, edgelist=None):
        if edgelist is None:
            edgelist = self.map.Graph.edges()

        for e in edgelist:

            pg.draw.line(
                self.surf, LINE_COLOR,
                (int((self.display_width) * self.map.pos[e[0]][0] + RADIUS),
                 int((self.display_width) * self.map.pos[e[0]][1] + RADIUS)),
                (int((self.display_height) * self.map.pos[e[1]][0] + RADIUS),
                 int((self.display_height) * self.map.pos[e[1]][1] + RADIUS)),
                5)

    def draw_node_labels(self, labels=None):
        if labels is None:
            labels = dict((n, n) for n in self.map.Graph.nodes())
        for v, label in labels.items():

            text = pg.font.Font(None, 25).render(
                str(label), False, POINT_LABEL_COLOR)
            text_pos_x = int((self.display_width) * self.map.pos[v][0] + RADIUS - (text.get_width() / 2))
            text_pos_y = int((self.display_height) * self.map.pos[v][1] + RADIUS- (text.get_height() / 2))
            self.surf.blit(
                text, (text_pos_x,text_pos_y))

    def draw_fps(self):
        self.surf.blit(
            pg.font.Font(None, 30).render(
                str('fps : %.1f' % self.clock.get_fps()), False, (255, 255, 255)),
            (self.display_width - 60, self.display_height - 20))

    def update(self):
        self.surf.blit(self.background, (0, 0))
        self.draw_edges()
        self.draw_points()
        self.draw_fps()
        self.draw_node_labels()

        self.screen.blit(self.surf, (0, 0))
        pg.display.update()

    def run(self):
        client = Runner()
        done = False
        try:
            status, start_data = client.remote_process_client.login(client.name)
            self.map = client.remote_process_client.read_map()
            while not done:
                self.update()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        done = True
                    if event.type == KEYDOWN:
                        if event.key == K_s:
                            done = True


                pg.display.flip()
                self.clock.tick(self.fps)
        finally:
            client.remote_process_client.logout()
            client.remote_process_client.close()
            pg.quit()


if __name__ == '__main__':
    gui = GUI()
    gui.run()
