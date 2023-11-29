import pygame
from math import sin, cos

WIDTH = 800
HEIGHT = 600

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

FPS = 48
VELOCITY = 100.0
ANGULAR_SPEED = 10.0
TOL = 1.0

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

