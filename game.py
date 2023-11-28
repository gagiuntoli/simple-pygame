import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

