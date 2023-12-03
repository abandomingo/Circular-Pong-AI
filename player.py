import pygame
import math

class Player:
    def __init__(self, player_angle, player_length, player_width, WIDTH, HEIGHT, screen, color, is_ai=False):
        self.player_angle = player_angle
        self.player_length = player_length
        self.player_width = player_width
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.color = color
        self.is_ai = is_ai

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

    def draw(self):
        # Draw the player line
        pygame.draw.polygon(self.screen, self.color, [(self.edge1_x, self.edge1_y), (self.edge2_x, self.edge2_y), (self.edge3_x, self.edge3_y), (self.edge4_x, self.edge4_y)])

    def get_position(self):
        # Return player position
        return self.edge1_x, self.edge1_y, self.edge2_x, self.edge2_y, self.edge3_x, self.edge3_y, self.edge4_x, self.edge4_y


