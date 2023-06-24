import pygame as pg
from settings import *

_=False

# TODO: read from file
_mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,1,1,1,_,_,_,_,_,_,_,_,_,_,_,1,_,_,1],
    [1,_,1,_,1,_,_,_,_,_,_,_,_,_,_,_,1,_,_,1],
    [1,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,1,_,1,_,1,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,1,_,_,_,1,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Map:
    def __init__(self, game):
        # create game reference
        self.game = game

        # add mini map to class
        self.mini_map = _mini_map
        
        # contains walls of map (x,y)
        self.world_map = {}

        # create world_map
        self.get_map()

    def get_map(self):
        # fill world_map

        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):

                if value:
                    self.world_map[(i,j)] = value
    
    def draw_minimap(self):
        for wall in self.world_map:
            pg.draw.rect(self.game.screen, 
                            (30,30,30), 
                            (wall[0] * MINIMAP_TILE_SIZE, wall[1] * MINIMAP_TILE_SIZE,
                            MINIMAP_TILE_SIZE, MINIMAP_TILE_SIZE),
                            2
                        )