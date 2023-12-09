#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (155, 89, 182)
CYAN = (0, 255, 255)
YELLOW = (244, 208, 63)
LGREEN = (46, 204, 113)
ORANGE = (211, 84, 0)
GRAY = (144, 148, 151)
PINK = (255, 153, 204)
playercolor = [BLUE, PURPLE, CYAN, YELLOW, PINK, LGREEN, ORANGE, GRAY]

#Screen Settings
WIDTH, HEIGHT = 900, 600
center = (WIDTH // 2, HEIGHT // 2)
FPS = 30

#Player Settings
how_many_real_players = 1  # up to 3
how_many_ai_players = 4 # any amount
player_speed = 5 #degrees per second
player_length = 10
player_width = 50
who_can_hit = 1 #who hits first

#Arena Settings
radius = 250 #arena radius

#Ball Settings
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 5
"Ball Initializers"
hit_count = 0
is_hit = False
"---------------"