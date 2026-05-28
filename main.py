import copy
import pygame
import sys

from scripts.tile import Tile
from scripts.entities import Entity
from scripts.formatter import format_level
from scripts.display import draw_grid, draw_entities, display_text
from scripts.movement import can_move, push, teleport
from scripts.locate import locate_tiles, locate_entities
from scripts.button_logic import update_gate_state
from scripts.levels import level_grids

pygame.init()

WIDTH = 736  # 23 tiles
HEIGHT = 480 # 15 tiles
TILE_SIZE = 32


screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)

levels = []
for level in level_grids:
    levels.append(format_level(level))
grids = []
level_entities = []
for level in levels:
    grids.append(level["grid"])
    level_entities.append(level["entities"])

current_level = 5

state = "game"

grid = copy.deepcopy(grids[current_level])
entities = copy.deepcopy(level_entities[current_level])

goal = locate_tiles(grid, "goal")[0]
button_positions = locate_tiles(grid, "button")
gate_positions = locate_tiles(grid, "gate")
portal_positions = locate_tiles(grid, "portal")

entity_positions = locate_entities(entities)
if state == "game":
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
            if state == "game":
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if can_move(entities, player, portal_positions, grid, 0, -1):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, 0, -1)
                        player.move(0,-1)
                        teleport(grid, entities, player, entity_positions, portal_positions, 0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if can_move(entities, player, portal_positions, grid, 0, 1):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, 0, 1)
                        player.move(0,1)
                        teleport(grid, entities, player, entity_positions, portal_positions, 0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if can_move(entities, player, portal_positions, grid, -1, 0):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, -1, 0)
                        player.move(-1,0)
                        teleport(grid, entities, player, entity_positions, portal_positions, -1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if can_move(entities, player, portal_positions, grid, 1, 0):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, 1, 0)
                        player.move(1,0)
                        teleport(grid, entities, player, entity_positions, portal_positions, 1, 0)
                entity_positions = locate_entities(entities)
                update_gate_state(grid, button_positions, gate_positions, entity_positions)
                if event.key == pygame.K_r:
                    grid = copy.deepcopy(grids[current_level])
                    entities = copy.deepcopy(level_entities[current_level])
                    player = Entity("player",0,0,(0,0,0))
                    for i in range(len(entities)):
                        if entities[i].entity_type == "player":
                            player = entities[i]
                entity_positions = locate_entities(entities)
                goal = locate_tiles(grid, "goal")[0]
                button_positions = locate_tiles(grid, "button")
                gate_positions = locate_tiles(grid, "gate")
                portal_positions = locate_tiles(grid, "portal")
                update_gate_state(grid, button_positions, gate_positions, entity_positions)


    if state == "game":
        draw_grid(screen, grid, TILE_SIZE)
        draw_entities(screen, entities, TILE_SIZE)
        if player.pos == goal:
            current_level += 1
            if current_level >= len(levels):
                current_level = 0
            grid = copy.deepcopy(grids[current_level])
            entities = copy.deepcopy(level_entities[current_level])
            player = Entity("player",0,0,(0,0,0))
            for i in range(len(entities)):
                if entities[i].entity_type == "player":
                    player = entities[i]
            entity_positions = locate_entities(entities)
            goal = locate_tiles(grid, "goal")[0]
            button_positions = locate_tiles(grid, "button")
            gate_positions = locate_tiles(grid, "gate")
            portal_positions = locate_tiles(grid, "portal")
            update_gate_state(grid, button_positions, gate_positions, entity_positions)
        display_text(screen, f"Level {current_level+1}", font, (255,255,255), 10, 10)
        pygame.display.update()
    

    clock.tick(360)
