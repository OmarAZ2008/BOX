import pygame

from scripts.tile import Tile

pygame.init()

def draw_grid(screen, grid: list[list[Tile]], TILE_SIZE: int):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tile = grid[i][j]
            rect = pygame.Rect(
                j*TILE_SIZE,
                i*TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, tile.color, rect)
            