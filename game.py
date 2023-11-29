import pygame
from math import sin, cos

WIDTH = 800
HEIGHT = 600

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 48
VELOCITY = 100.0
ANGULAR_SPEED = 10.0
TOL = 1.0
MIN_PLAYERS = 1
MAX_PLAYERS = 3

pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

is_running = True

position = (10.0, 100.0)
angle = 0.1

visited = []

def distance2(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return (x2-x1)**2 + (y2-y1)**2

def check_collision(position, visited, width, height):
    (x, y) = position
    if x < 0 or y < 0 or x > width or y > height:
        return True

    for point in visited:
        if distance2(position, point) < TOL:
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

players = get_players(screen, clock)

screen.fill(BLACK)

while is_running:

    dt = clock.tick(FPS)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_m]:
        angle += ANGULAR_SPEED * dt
    if keys[pygame.K_k]:
        angle -= ANGULAR_SPEED * dt

    (x, y) = position
    (vx, vy) = (VELOCITY * cos(angle), VELOCITY * sin(angle))

    if check_collision((x+vx*dt, y+vy*dt), visited, WIDTH, HEIGHT):
        new_position = position
        print("Game Over")
    else:
        new_position = (x+vx*dt, y+vy*dt)

    pygame.draw.line(screen, GREEN, position, new_position, width=3)

    pygame.display.update()

    position = new_position
    visited.append(position)

