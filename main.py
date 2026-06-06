import copy
import json
import pygame
import sys

from scripts.tile import Tile
from scripts.entities import Entity
from scripts.menus import Menu, draw_menu
from scripts.formatter import format_level
from scripts.display import draw_grid, draw_entities, display_text
from scripts.movement import can_move, push, teleport
from scripts.locate import locate_tiles, locate_entities
from scripts.button_logic import update_gate_state
from scripts.parser import parsed_levels

pygame.init()
pygame.mixer.init()

def play_sound(sound, sfx: bool):
    if sfx:
        sound.play()

title_bg = pygame.image.load("images/title_bg.png")

WIDTH = 736  # 23 tiles
HEIGHT = 480 # 15 tiles
TILE_SIZE = 32

sfx = True
bgm = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BOX")

screen.blit(title_bg, (0,0))
pygame.display.update()

font = pygame.font.SysFont(None, 36)

move_sound = pygame.mixer.Sound("sounds/move.ogg")
win_sound = pygame.mixer.Sound("sounds/win.ogg")

levels = []
for level in parsed_levels:
    levels.append(format_level(level))
grids = []
level_entities = []
for level in levels:
    grids.append(level["grid"])
    level_entities.append(level["entities"])

current_level = 0

state = "title"

unlocked_levels = [0]

try:
    with open("save.json", "r") as file:
        save_data = json.load(file)

    sfx = save_data["sfx"]
    unlocked_levels = save_data["unlocked_levels"]

except FileNotFoundError:
    sfx = True
    unlocked_levels = [0]

def save_game():
    save_data = {
        "sfx": sfx,
        "unlocked_levels": unlocked_levels
    }

    with open("save.json", "w") as file:
        json.dump(save_data, file)

title_menu = Menu("title", [{"text":"Levels", "color":(255,255,255)}, {"text":"SFX:ON", "color":(255,255,255)}, {"text":"Controls", "color":(255,255,255)}], 0)
controls_menu = Menu("controls", [{"text":"WASD/Arrows: Movement", "color":(255,255,255)}, {"text":"R: Reset Level", "color":(255,255,255)}, {"text":"Esc: Back", "color":(255,255,255)}, {"text":"SPACE: Select", "color":(255,255,255)}], 0)
levels_menu = Menu("levels", [{"text":"1", "color":(255,255,255)}, {"text":"2", "color":(60,60,60)}, {"text":"3", "color":(60,60,60)}, {"text":"4", "color":(60,60,60)}, {"text":"5", "color":(60,60,60)}, {"text":"6", "color":(60,60,60)}, {"text":"7", "color":(60,60,60)}, {"text":"8", "color":(60,60,60)}, {"text":"9", "color":(60,60,60)}, {"text":"10", "color":(60,60,60)}], 0)
max_level = len(levels_menu.options) - 1

if sfx:
    title_menu.options[1]["text"] = "SFX:ON"
else:
    title_menu.options[1]["text"] = "SFX:OFF"
def update_unlocked_levels(unlocked_levels):
    for option in levels_menu.options:
        level = int(option["text"]) - 1
        if level in unlocked_levels and level != levels_menu.selected_option:
            option["color"] = (255,255,255)

    
  
    


grid = copy.deepcopy(grids[current_level])
entities = copy.deepcopy(level_entities[current_level])

entity_positions = locate_entities(entities)
goal = locate_tiles(grid, "goal")[0]
button_positions = locate_tiles(grid, "button")
gate_positions = locate_tiles(grid, "gate")
portal_positions = locate_tiles(grid, "portal")
update_gate_state(grid, button_positions, gate_positions, entity_positions, sfx)

current_menu = title_menu

entity_positions = locate_entities(entities)
if state == "game":
    update_gate_state(grid, button_positions, gate_positions, entity_positions, sfx)

player = Entity("player",0,0,(0,0,0))
for i in range(len(entities)):
    if entities[i].entity_type == "player":
        player = entities[i]


clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if state == "game":
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if can_move(entities, player, portal_positions, grid, 0, -1):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, 0, -1, sfx)
                        player.move(0,-1)
                        teleport(grid, entities, player, entity_positions, portal_positions, 0, -1, sfx)
                        play_sound(move_sound, sfx)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if can_move(entities, player, portal_positions, grid, 0, 1):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, 0, 1, sfx)
                        player.move(0,1)
                        teleport(grid, entities, player, entity_positions, portal_positions, 0, 1, sfx)
                        play_sound(move_sound, sfx)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if can_move(entities, player, portal_positions, grid, -1, 0):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, -1, 0, sfx)
                        player.move(-1,0)
                        teleport(grid, entities, player, entity_positions, portal_positions, -1, 0, sfx)
                        play_sound(move_sound, sfx)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if can_move(entities, player, portal_positions, grid, 1, 0):
                        push(grid, entities, entity_positions, portal_positions, player.x, player.y, 1, 0, sfx)
                        player.move(1,0)
                        teleport(grid, entities, player, entity_positions, portal_positions, 1, 0, sfx)
                        play_sound(move_sound, sfx)
                elif event.key == pygame.K_ESCAPE:
                    grid = copy.deepcopy(grids[current_level])
                    entities = copy.deepcopy(level_entities[current_level])
                    player = Entity("player",0,0,(0,0,0))
                    for i in range(len(entities)):
                        if entities[i].entity_type == "player":
                            player = entities[i]
                    state = "levels"
                    current_menu = levels_menu
                for i in range(len(entities)):
                    if entities[i].entity_type == "player":
                        entities[i] = player
                entity_positions = locate_entities(entities)
                update_gate_state(grid, button_positions, gate_positions, entity_positions, sfx)
                if event.key == pygame.K_r:
                    grid = copy.deepcopy(grids[current_level])
                    entities = copy.deepcopy(level_entities[current_level])
                    player = Entity("player",0,0,(0,0,0))
                    for i in range(len(entities)):
                        if entities[i].entity_type == "player":
                            player = entities[i]
                    entity_positions = locate_entities(entities)
                    update_gate_state(grid, button_positions, gate_positions, entity_positions, sfx)
                
            elif state == "title":
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    current_menu.move_up()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    current_menu.move_down()
                elif event.key == pygame.K_SPACE:
                    option = current_menu.options[current_menu.selected_option]
                    if "SFX" in option["text"]:
                        if "ON" in option["text"]:
                            option["text"] = "SFX:OFF"
                            sfx = False
                        elif "OFF" in option["text"]:
                            option["text"] = "SFX:ON"
                            sfx = True
                        save_game()
                    elif "Controls" in option["text"]:
                        state = "controls"
                        current_menu = controls_menu
                    elif "Levels" in option["text"]:
                        state = "levels"
                        current_menu = levels_menu
            elif state == "controls":
                if event.key == pygame.K_ESCAPE:
                    state = "title"
                    current_menu = title_menu
            elif state == "levels":
                if event.key == pygame.K_ESCAPE:
                    state = "title"
                    current_menu = title_menu
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    current_menu.move_left(unlocked_levels, max_level)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    current_menu.move_right(unlocked_levels, max_level)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    current_menu.move_level_up(unlocked_levels)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    current_menu.move_level_down(unlocked_levels, max_level)
                elif event.key == pygame.K_SPACE:
                    state = "game"
                    current_level = current_menu.selected_option
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
                    update_gate_state(grid, button_positions, gate_positions, entity_positions, sfx)
                    current_menu = Menu("", [{"text":"TEXT", "color":(255,255,255)}], 0)
                

    if state == "game":
        draw_grid(screen, grid, TILE_SIZE)
        draw_entities(screen, entities, TILE_SIZE)
        if player.pos == goal:
            play_sound(win_sound, sfx)
            current_level += 1
            if current_level >= len(levels):
                current_level = 0
            if current_level not in unlocked_levels:
                unlocked_levels.append(current_level)
            save_game()
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
            update_gate_state(grid, button_positions, gate_positions, entity_positions, sfx)
        display_text(screen, f"Level {current_level+1}", font, (255,255,255), 10, 10)
        pygame.display.update()
    elif state == "title":
        screen.blit(title_bg, (0,0))
        draw_menu(current_menu, 72, screen, WIDTH, HEIGHT)
        pygame.display.update()
    elif state == "controls":
        draw_menu(current_menu, 48, screen, WIDTH, HEIGHT)
        pygame.display.update()
    elif state == "levels":
        draw_menu(current_menu, 48, screen, WIDTH, HEIGHT)
        update_unlocked_levels(unlocked_levels)
        pygame.display.update()

    clock.tick(60)
