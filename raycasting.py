import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game) -> None:
        self.game = game
    
    def ray_cast(self):
        # get curr pos
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        # get angle of first left ray
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001 

        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map+1,1) if sin_a >0 else (y_map-1e-6, -1)

            deph_hor = (y_hor-oy) / sin_a
            x_hor = ox + deph_hor * cos_a

            delta_depth = dy/ sin_a
            dx = delta_depth*cos_a

            for i in range(MAX_DEPH):
                tile_vert = int(x_hor), int(y_hor)
                if tile_vert in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                deph_hor += delta_depth

            # vertal collision
            x_vert, dx  = (x_map + 1, 1) if cos_a >0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox)/cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
            
            # depth
            depth = min(depth_vert, deph_hor)
            
            pg.draw.line(self.game.screen,
                        (255,0,0),
                        (MINIMAP_TILE_SIZE*ox, MINIMAP_TILE_SIZE*oy),
                        (MINIMAP_TILE_SIZE*(ox + depth*cos_a), MINIMAP_TILE_SIZE*(oy+depth*sin_a)),
                        2
                        )
            
            ray_angle +=DELTA_ANGLE
        
    def update(self):
        self.ray_cast()