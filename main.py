import pygame
import sys

from scripts.tile import Tile

pygame.init()

WIDTH = 704  # 22 tiles
HEIGHT = 480 # 15 tiles
TILE_SIZE = 32


a = Tile("wall", (1,1,1), False)

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
