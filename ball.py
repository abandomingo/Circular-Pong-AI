import pygame
import sys
import math
import random
from constants import *

class Ball:
    def __init__(self, ball_pos, ball_speed, ball_radius, WIDTH, HEIGHT, screen):
        self.ball_pos = ball_pos
        self.ball_speed = ball_speed
        self.ball_radius = ball_radius
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen

    def update(self, player_positions, hit_count, is_hit, player_angles, ball_speed):
        # Update ball position
        hit_count = hit_count
        is_out = False
        self.ball_pos[0] += self.ball_speed[0] 
        self.ball_pos[1] += self.ball_speed[1] 

        # Check if the ball crosses the boundary of the circular play area
        distance_to_center = math.sqrt((self.ball_pos[0] - self.WIDTH // 2) ** 2 + (self.ball_pos[1] - self.HEIGHT // 2) ** 2)
        if distance_to_center + self.ball_radius >= radius:  # If the ball is outside the circular boundary
            #reset ball position
            self.ball_pos[0] = self.WIDTH // 2
            self.ball_pos[1] = self.HEIGHT // 2
            self.ball_speed = ball_speed
            is_out = True

        # Draw the ball
        pygame.draw.circle(self.screen, RED, (int(self.ball_pos[0]), int(self.ball_pos[1])), self.ball_radius)

        # Check collision with the ball
        for index, player_cord in enumerate(player_positions):
            if not player_cord:
                continue
            
            edge1_x, edge1_y, edge2_x, edge2_y, edge3_x, edge3_y, edge4_x, edge4_y = player_cord

            if (
                self.ball_pos[0] <= max(edge1_x, edge2_x, edge3_x, edge4_x) and
                self.ball_pos[0] >= min(edge1_x, edge2_x, edge3_x, edge4_x) and
                self.ball_pos[1] <= max(edge1_y, edge2_y, edge3_y, edge4_y) and
                self.ball_pos[1] >= min(edge1_y, edge2_y, edge3_y, edge4_y) and
                not is_hit
                ):
                self._handle_collision(player_angles[index], hit_count)
                return True, is_out

        return False, is_out

    def _handle_collision(self, player_angle, hit_count):
        if 0 < player_angle <= 90:
            self._reflect_ball(1, 1, hit_count)
        elif 90 < player_angle <= 180:
            self._reflect_ball(-1, 1, hit_count)
        elif 180 < player_angle <= 270:
            self._reflect_ball(-1, -1, hit_count)
        elif 270 < player_angle <= 360:
            self._reflect_ball(1, -1, hit_count)

    def _reflect_ball(self, x_direction, y_direction, hit_count):
        speed_factor = random.choice([2, 3, 4]) + (hit_count/4)
        self.ball_speed[0] = x_direction * abs(speed_factor)
        speed_factor = random.choice([2, 3, 4]) + (hit_count/4)
        self.ball_speed[1] = y_direction * abs(speed_factor)

        # Ball collided with the player line, reflect the ball
        self.ball_speed[0] *= -1
        self.ball_speed[1] *= -1