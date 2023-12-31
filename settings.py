from math import pi, tan

# GAME
FPS = 60
WND_WIDTH, WND_HEIGHT =  800, 600
WND_WIDTH_HALF, WND_HEIGHT_HALF = WND_WIDTH//2, WND_HEIGHT//2

# PLAYER
PLAYER_POS = 1.5, 5 #minimap pos
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

PLAYER_RADIUS = 0.3 # minimap size

# RAYCASTING
FOV = pi/3
HALF_FOV = FOV/2
NUM_RAYS = WND_WIDTH//2
DELTA_ANGLE = FOV/NUM_RAYS
MAX_DEPH = 20

SCREEN_DIST = WND_WIDTH_HALF/tan(HALF_FOV)
PROJECTION_SCALE = WND_WIDTH//NUM_RAYS

# MINI MAP
MINIMAP_TILE_SIZE = 40

# TEXTURES
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE//2