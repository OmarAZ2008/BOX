import pygame
import sys

pygame.init()

WIDTH = 720
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = [
[],
]



clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.fill((0, 0, 0))

    pygame.display.update()

    clock.tick(60)
