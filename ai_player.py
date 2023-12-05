import math
import random
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


    #FUTURE AI IMPLEMENTATIONS
    """def pick_movement(self, ball_pos, player_angle, center):

        move = random.choice([self.move_left_towards_ball( ball_pos, player_angle, center),
                            self.move_right_towards_ball( ball_pos, player_angle, center),])
        return move

    def move_left_towards_ball(self, ball_pos, player_angle, center):
        target_angle = self._calculate_ball_angle(center, ball_pos)
        self.calculate_position()  # Recalculate the position
    
        if abs(player_angle - target_angle) <= 5:
            move = 'STAY'
        else:
            move ='MOVE_LEFT'
        return move

    def move_right_towards_ball(self, ball_pos, player_angle, center):
        target_angle = self._calculate_ball_angle(center, ball_pos)
        self.calculate_position()  # Recalculate the position
    
        if abs(player_angle - target_angle) <= 1:
            move = 'STAY'
        else:
            move ='MOVE_RIGHT'
        return move"""

    """def move_towards_ball(self, ball_pos, player_angle, center):
            target_angle = self._calculate_ball_angle(center, ball_pos)
            self.calculate_position()  # Recalculate the position

            choose_right = math.atan2(player_angle - target_angle, target_angle)
            choose_left = math.atan2(target_angle - player_angle, player_angle)

            if abs(player_angle - target_angle) <= 1:
                move = 'STAY'
            elif choose_right < choose_left:
                move = 'MOVE_LEFT'
                print(choose_left)
                print(choose_right)
            elif choose_left < choose_right:
                move = 'MOVE_RIGHT'
                print(choose_left)
                print(choose_right)
            return move"""

    #BASIC PLAYER AI
    def move_towards_ball(self, ball_pos, player_angle, center):
                target_angle = self._calculate_ball_angle(center, ball_pos)
                self.calculate_position()  # Recalculate the position

                choose_right = (player_angle - target_angle)
                choose_left = (target_angle - player_angle)

                if abs(player_angle - target_angle) <= 1:
                    move = 'STAY'
                elif choose_right < choose_left:
                    move = 'MOVE_LEFT'
                elif choose_left < choose_right:
                    move = 'MOVE_RIGHT'
                else:
                    move = 'STAY'
                return move

    def _calculate_ball_angle(self, center, ball_pos):
        dx = ball_pos[0] - center[0]
        dy = ball_pos[1] - center[1]

        # Use arctangent to calculate the angle in radians
        angle_rad = math.atan2(dy, dx)

        # Convert radians to degrees
        angle_deg = math.degrees(angle_rad)

        # Convert negative angles to positive equivalent in the custom format
        if angle_deg < 0:
            angle_deg = 360 + angle_deg

        return angle_deg


