import pygame
import sys

from scripts.tile import Tile
from scripts.grid_formatter import format_grid
from scripts.draw import draw_grid
from scripts.levels import level_1

pygame.init()

WIDTH = 704  # 22 tiles
HEIGHT = 480 # 15 tiles
TILE_SIZE = 32


a = Tile("wall", (1,1,1), False)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = format_grid(level_1)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_grid(screen, grid, TILE_SIZE)
    pygame.display.update()
    

    clock.tick(60)
