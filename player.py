import pygame as pg
import math


from settings import *

class Player:
    def __init__(self,game):
        # hold reference to game object
        self.game = game

        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time

        speed_sin = sin_a * speed
        speed_cos = cos_a * speed

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        # allow movement if no collision occur
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy
        
        # rotation controlls
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time

        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        # make sure angle < 2*pi
        self.angle %= math.tau
    
    def draw_minimap(self):
        # draw view line
        #pg.draw.line(self.game.screen,
        #                (255,255,0),
        #                (self.x * MINIMAP_TILE_SIZE, self.y * MINIMAP_TILE_SIZE),
        #                (self.x * MINIMAP_TILE_SIZE + math.cos(self.angle) * 2 *MINIMAP_TILE_SIZE, 
        #                self.y * MINIMAP_TILE_SIZE + math.sin(self.angle) * 2 *MINIMAP_TILE_SIZE),
        #                 1
        #            )

        # draw player
        pg.draw.circle(self.game.screen,
                        (0,240,0), 
                        (self.x * MINIMAP_TILE_SIZE, self.y * MINIMAP_TILE_SIZE),
                        MINIMAP_TILE_SIZE*PLAYER_RADIUS
                    )

    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map    
            
    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)

