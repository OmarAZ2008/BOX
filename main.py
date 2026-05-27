import pygame
import sys

from scripts.tile import Tile
from scripts.entities import Entity
from scripts.grid_formatter import format_grid
from scripts.display import draw_grid, draw_entities, display_text
from scripts.movement import can_move, push
from scripts.locate import locate_tiles, locate_entities
from scripts.levels import level_1

pygame.init()

WIDTH = 704  # 22 tiles
HEIGHT = 480 # 15 tiles
TILE_SIZE = 32


screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)

grid = format_grid(level_1)

goal = locate_tiles(grid, "goal")[0]

start_x = 8
start_y = 10
box_x = 12
box_y = 8
player_color = (0,120,255)
box_color = (160,110,60)
player = Entity(start_x, start_y, player_color)
box = Entity(box_x, box_y, box_color)
entities = [player, box, Entity(12,10,box_color)]
entity_positions = locate_entities(entities)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if can_move(entities, player, grid, 0, -1):
                    push(entities, entity_positions, player.x, player.y, 0, -1)
                    player.move(0,-1)
            elif event.key == pygame.K_DOWN:
                if can_move(entities, player, grid, 0, 1):
                    push(entities, entity_positions, player.x, player.y, 0, 1)
                    player.move(0,1)
            elif event.key == pygame.K_LEFT:
                if can_move(entities, player, grid, -1, 0):
                    push(entities, entity_positions, player.x, player.y, -1, 0)
                    player.move(-1,0)
            elif event.key == pygame.K_RIGHT:
                if can_move(entities, player, grid, 1, 0):
                    push(entities, entity_positions, player.x, player.y, 1, 0)
                    player.move(1,0)
            entity_positions = locate_entities(entities)
    
    
    draw_grid(screen, grid, TILE_SIZE)
    draw_entities(screen, entities, TILE_SIZE)
    if player.pos == goal:
        text = "Congratulations! You Win"
        display_text(screen, text, font, (255,255,255), 10, 10)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    

    clock.tick(60)
