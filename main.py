import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
import pygame as pg

from settings import *
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer

class Game:
    def __init__(self) -> None:
        # setup pygame
        pg.init()
        self.screen = pg.display.set_mode((WND_WIDTH, WND_HEIGHT))
        self.clock = pg.time.Clock()
        self.delta_time = 1

        # start new game
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
    
    def update(self):
        self.raycasting.update()

        # update the screen
        pg.display.flip()
    
        # update the clock :/
        self.delta_time = self.clock.tick(FPS)

        # update player
        self.player.update()

        # debug set fps as title of screen
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        # paint the screen black
        self.screen.fill((0,0,0))

        # draw minimap *debug
        #self.map.draw_minimap()
        #self.raycasting.update()

        # draw debug player on minimap
        #self.player.draw_minimap()
    
    def check_events(self):
        # event pull
        for e in pg.event.get():

            # handle exit events
            if e.type == pg.QUIT or \
                (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):

                # quit pygame
                pg.quit()
                # exit app
                sys.exit()
            
    def run(self):
        while 1:
            self.check_events()
            self.update()
            self.draw()


# example game
if __name__ == '__main__':
    g = Game()
    g.run()
