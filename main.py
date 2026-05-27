import pygame
import sys

from scripts.tile import Tile
from scripts.entities import Entity
from scripts.formatter import format_level
from scripts.display import draw_grid, draw_entities, display_text
from scripts.movement import can_move, push, teleport
from scripts.locate import locate_tiles, locate_entities
from scripts.button_logic import update_gate_state
from scripts.levels import level_1_grid

pygame.init()

WIDTH = 704  # 22 tiles
HEIGHT = 480 # 15 tiles
TILE_SIZE = 32


screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)

formatted_level = format_level(level_1_grid)
grid = formatted_level["grid"]

goal = locate_tiles(grid, "goal")[0]
button_positions = locate_tiles(grid, "button")
gate_positions = locate_tiles(grid, "gate")
portal_positions = locate_tiles(grid, "portal")

entities = formatted_level["entities"]
entity_positions = locate_entities(entities)

update_gate_state(grid, button_positions, gate_positions, entity_positions)

player = Entity("player",0,0,(0,0,0))
for i in range(len(entities)):
    if entities[i].entity_type == "player":
        player = entities[i]


clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if can_move(entities, player, portal_positions, grid, 0, -1):
                    push(grid, entities, entity_positions, portal_positions, player.x, player.y, 0, -1)
                    player.move(0,-1)
                    teleport(grid, entities, player, entity_positions, portal_positions, 0, -1)
            elif event.key == pygame.K_DOWN:
                if can_move(entities, player, portal_positions, grid, 0, 1):
                    push(grid, entities, entity_positions, portal_positions, player.x, player.y, 0, 1)
                    player.move(0,1)
                    teleport(grid, entities, player, entity_positions, portal_positions, 0, 1)
            elif event.key == pygame.K_LEFT:
                if can_move(entities, player, portal_positions, grid, -1, 0):
                    push(grid, entities, entity_positions, portal_positions, player.x, player.y, -1, 0)
                    player.move(-1,0)
                    teleport(grid, entities, player, entity_positions, portal_positions, -1, 0)
            elif event.key == pygame.K_RIGHT:
                if can_move(entities, player, portal_positions, grid, 1, 0):
                    push(grid, entities, entity_positions, portal_positions, player.x, player.y, 1, 0)
                    player.move(1,0)
                    teleport(grid, entities, player, entity_positions, portal_positions, 1, 0)
            entity_positions = locate_entities(entities)
            update_gate_state(grid, button_positions, gate_positions, entity_positions)
    
    
    draw_grid(screen, grid, TILE_SIZE)
    draw_entities(screen, entities, TILE_SIZE)
    if player.pos == goal:
        text = "Congratulations! You Win"
        display_text(screen, text, font, (255,255,255), 10, 10)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    

    clock.tick(360)
