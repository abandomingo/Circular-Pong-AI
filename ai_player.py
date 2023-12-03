import math
from player import Player
from colors import *

class AIPlayer(Player):
    def __init__(self, player_angle, player_length, player_width, WIDTH, HEIGHT, screen, color, is_ai=True, ai_speed=5):
        super().__init__(player_angle, player_length, player_width, WIDTH, HEIGHT, screen, color, is_ai)
        self.ai_speed = ai_speed
        self.is_ai = True
        self.target_angle = self.player_angle  # Initialize the target angle

    def calculate_position(self):
        # Calculate player position along the inner circle
        self.player_x = self.WIDTH // 2 + int(200 * math.cos(math.radians(self.player_angle)))
        self.player_y = self.HEIGHT // 2 + int(200 * math.sin(math.radians(self.player_angle)))

        # Calculate the endpoint of the player line
        self.end_x = self.player_x + int(self.player_length * math.cos(math.radians(self.player_angle)))
        self.end_y = self.player_y + int(self.player_length * math.sin(math.radians(self.player_angle)))

        # Calculate the perpendicular vector to the player line
        perp_vector_x = -math.sin(math.radians(self.player_angle))
        perp_vector_y = math.cos(math.radians(self.player_angle))

        # Calculate the points for the two edges of the player line
        self.edge1_x = self.player_x + int(self.player_width / 2 * perp_vector_x)
        self.edge1_y = self.player_y + int(self.player_width / 2 * perp_vector_y)

        self.edge2_x = self.end_x + int(self.player_width / 2 * perp_vector_x)
        self.edge2_y = self.end_y + int(self.player_width / 2 * perp_vector_y)

        self.edge3_x = self.end_x - int(self.player_width / 2 * perp_vector_x)
        self.edge3_y = self.end_y - int(self.player_width / 2 * perp_vector_y)

        self.edge4_x = self.player_x - int(self.player_width / 2 * perp_vector_x)
        self.edge4_y = self.player_y - int(self.player_width / 2 * perp_vector_y)

    def move_towards_ball(self, ball_pos):
        self.calculate_position()  # Recalculate the position

        # Calculate the angle towards the ball
        self.target_angle = math.degrees(math.atan2(ball_pos[1] - self.player_y, ball_pos[0] - self.player_x))

        # Smoothly move towards the target angle
        angle_difference = (self.target_angle - self.player_angle) % 360

        if abs(angle_difference) <= 30:
            self.player_angle = self.target_angle
            move = 'STAY'
        elif angle_difference > self.ai_speed:
            self.player_angle = (self.player_angle + self.ai_speed) % 360
            move = 'MOVE_LEFT'
        else:
            self.player_angle = (self.player_angle - self.ai_speed) % 360
            move = 'MOVE_RIGHT'

        return move
    
    def calculate_new_position(ball_pos, slope, delta_x):
        x, y = ball_pos
        new_x = x + delta_x
        new_y = y + slope * delta_x
        return new_x, new_y
        
    def calculate_new_ball_position(self, ball_pos, delta_x):
        slope = math.tan(math.radians(self.target_angle))  # Calculate slope using target_angle
        new_ball_pos = self.calculate_new_position(ball_pos, slope, delta_x)
        return new_ball_pos
