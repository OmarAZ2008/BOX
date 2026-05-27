import pygame

from scripts.tile import Tile
from scripts. entities import Entity

pygame.init()

def draw_grid(screen, grid: list[list[Tile]], TILE_SIZE: int):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tile = grid[i][j]
            rect = pygame.Rect(
                j * TILE_SIZE,
                i * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, tile.color, rect)

def draw_entity(screen, entity: Entity, TILE_SIZE: int):
    rect = pygame.Rect(
        entity.x * TILE_SIZE,
        entity.y * TILE_SIZE,
        TILE_SIZE,
        TILE_SIZE
    )
    pygame.draw.rect(screen, entity.color, rect)

def display_text(screen, text, font, color, x, y):
    text_surface = font.render(text,True,color)
    screen.blit(text_surface, (x, y))