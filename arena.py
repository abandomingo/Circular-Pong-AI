import pygame
import sys
import math
import random
from colors import *

def Arena(WIDTH, HEIGHT, screen):
    # Circular arena with white border (outline)
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 5, 3)
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 250, 5)  # Outline with thickness 5 pixels
