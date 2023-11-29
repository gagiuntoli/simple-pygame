import pygame
from math import sin, cos, pi
from random import randrange, random

WIDTH = 800
HEIGHT = 600

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 48
VELOCITY = 100.0
ANGULAR_SPEED = 10.0
MIN_PLAYERS = 1
MAX_PLAYERS = 3

class Player:
    def __init__(self, name, color, keys):
        self.name = name
        self.position = (randrange(0, WIDTH), randrange(0, HEIGHT))
        self.angle = random() * 2 * pi
        self.color = color
        self.keys = keys
        self.alive = True

pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

is_running = True

visited = []

def distance2(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return (x2-x1)**2 + (y2-y1)**2

def check_collision(position, visited, width, height, dt):
    (x, y) = position
    if x < 0 or y < 0 or x > width or y > height:
        return True

    for point in visited:
        if distance2(position, point) < (VELOCITY * dt)**2 + 1e-6:
            return True

    return False

def get_players(screen, clock):
    players = []
    num_players = MIN_PLAYERS
    num_players_selected = False

    font = pygame.font.SysFont('Comic Sans MS', 40)
    name = ''

    while True:
        for event in pygame.event.get():
            if not num_players_selected:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and num_players > MIN_PLAYERS:
                        num_players -= 1
                    if event.key == pygame.K_UP and num_players < MAX_PLAYERS:
                        num_players += 1
                    if event.key == pygame.K_RETURN:
                        num_players_selected = True
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        players.append(name)
                        name = ''
                        if len(players) == num_players:
                            return players
                    elif event.key in [pygame.K_DELETE, pygame.K_BACKSPACE]:
                        name = name[:len(name)-1]
                    else:
                        name += event.unicode

        screen.fill(BLACK)
        screen.blit(font.render('Select number of players: '+str(num_players), False, RED), (100,100))

        if num_players_selected:
            for i, player in enumerate(players):
                screen.blit(font.render('Player '+str(i+1)+': '+player, False, RED), (100,150+i*50))
            screen.blit(font.render('Player '+str(len(players)+1)+': '+name, False, RED), (100,150+len(players)*50))


        pygame.display.update()
        clock.tick(FPS)

players_name = get_players(screen, clock)

colors = [RED, GREEN, BLUE]
keys = [
    (pygame.K_m, pygame.K_k),
    (pygame.K_v, pygame.K_b),
    (pygame.K_a, pygame.K_z)
]
players = [Player(name, colors[i], keys[i]) for i, name in enumerate(players_name)]

def check_winner(players):
    if len(players) <= 1:
        return None
    alives = [player.alive for player in players].count(True)
    if alives == 1:
        index = [player.alive for player in players].index(True)
        return players[index].name
    return None

screen.fill(BLACK)

while is_running:

    dt = clock.tick(FPS)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys=pygame.key.get_pressed()
    for player in players:

        if player.alive:
            (key_1, key_2) = player.keys
            if keys[key_1]:
                player.angle += ANGULAR_SPEED * dt
            if keys[key_2]:
                player.angle -= ANGULAR_SPEED * dt

            (x, y) = player.position
            (vx, vy) = (VELOCITY * cos(player.angle), VELOCITY * sin(player.angle))

            if check_collision((x+vx*dt, y+vy*dt), visited, WIDTH, HEIGHT, dt):
                player.alive = False
                continue
            else:
                new_position = (x+vx*dt, y+vy*dt)

            pygame.draw.line(screen, player.color, player.position, new_position, width=3)

            visited.append(player.position)
            player.position = new_position


    # Check for winner
    winner = check_winner(players)
    if winner:
        font = pygame.font.SysFont('Comic Sans MS', 40)
        screen.blit(font.render('player '+winner+ ' won!', False, RED), (WIDTH//2,HEIGHT//2))


    pygame.display.update()

