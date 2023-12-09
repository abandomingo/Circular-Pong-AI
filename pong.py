import sys
import math
import random
import pygame
from arena import Arena
from ball import Ball
from player import Player
from ai_player import AIPlayer
from constants import *

pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circular Pong")
clock = pygame.time.Clock()

players = []
total_players = how_many_ai_players + how_many_real_players


#Create the players with basic 
for player in range(how_many_real_players):
    player_angle = 360 / total_players * (player + 1)
    players.append({'player_angle': player_angle, 'player_length': player_length, 'player_width': player_width,  'is_ai': False})

for player in range(how_many_ai_players):
    player_angle = 360 / total_players * (player + how_many_real_players)
    players.append({'player_angle': player_angle, 'player_length': player_length, 'player_width': player_width, 'is_ai': True})



ball_speed = random.choice([[-3, -3], [3, 3], [-3, 3], [3, -3]])

player_positions = []
player_angles = []

# Initialize the Ball
ball = Ball(ball_pos, ball_speed, 5, WIDTH, HEIGHT, screen)

def move_right(player_num):
    players[player_num]['player_angle'] -= player_speed
    players[player_num]['player_angle'] %= 360

def move_left(player_num):
    players[player_num]['player_angle'] += player_speed
    players[player_num]['player_angle'] %= 360

def player_movement(keys):
    if keys[pygame.K_RIGHT]:
        move_right(0)
    if keys[pygame.K_LEFT]:
        move_left(0)
    if keys[pygame.K_d]:
        move_right(1)
    if keys[pygame.K_a]:
        move_left(1)
    if keys[pygame.K_l]:
        move_right(2)
    if keys[pygame.K_j]:
        move_left(2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_movement(keys)

    screen.fill(BLACK) 
    Arena(WIDTH, HEIGHT, screen)

    for index, player in enumerate(players):
        if(player['is_ai'] == True):
            ai_player = AIPlayer(player['player_angle'], player['player_length'], player['player_width'], WIDTH, HEIGHT, screen, RED if index == who_can_hit else playercolor[index])
            if(index == who_can_hit):
                if(index % 2 == 0):
                    move = ai_player.move_towards_ball(ball.ball_pos, ai_player.player_angle, center)
                elif(index % 2 == 1):
                    move = ai_player.move_towards_ball(ball.ball_pos, ai_player.player_angle, center)

                if(move == 'MOVE_RIGHT'):
                    move_right(index)
                elif(move == 'MOVE_LEFT'):
                    move_left(index)
                else:
                    pass
            ai_player.calculate_position()
            ai_player.draw()
            if(index == who_can_hit):
                player_positions.append(ai_player.get_position())
            else:
                player_positions.append([])
        else:
            current_player = Player(player['player_angle'], player['player_length'], player['player_width'], WIDTH, HEIGHT, screen, RED if index == who_can_hit else WHITE)
            current_player.calculate_position()
            current_player.draw()
            if(index == who_can_hit):
                player_positions.append(current_player.get_position())
            else:
                player_positions.append([])

    player_angles = [player['player_angle'] for player in players]

    is_hit, is_out = ball.update(player_positions, hit_count, is_hit, player_angles, ball_speed)

    player_angles = []
    player_positions = []

    if(is_hit):
        hit_count = hit_count + 1
        who_can_hit = (who_can_hit + 1) % (how_many_real_players + how_many_ai_players) 

    if(is_out):
        ball_direction = random.choice([[-3, -3], [3, 3], [-3, 3], [3, -3]])
        ball_speed = ball_direction
        hit_count = 0
        if(how_many_real_players + how_many_ai_players > 0):
            who_can_hit = (who_can_hit + 1) % (how_many_real_players + how_many_ai_players)

    # Display hit count
    hit_count_text = font20.render(f"Hit Count: {hit_count}", True, WHITE)
    screen.blit(hit_count_text, (WIDTH // 2 - 80, 10))

    pygame.display.flip()
    clock.tick(FPS)

