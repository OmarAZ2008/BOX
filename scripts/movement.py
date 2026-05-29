import pygame

from scripts.entities import Entity
from scripts.tile import Tile
from scripts.locate import locate_entities

pygame.init()
pygame.mixer.init()

teleport_sound = pygame.mixer.Sound("sounds/portal.ogg")

def play_sound(sound, sfx: bool):
    if sfx:
        sound.play()

def out_of_bounds(grid, new_x, new_y):
    rows = len(grid)
    cols = len(grid[0])

    if new_x < 0 or new_x >= cols:
        return True
    if new_y < 0 or new_y >= rows:
        return True
    return False

def new_tile_solid(grid, new_x, new_y):
    tile = grid[new_y][new_x]
    if tile.solid:
        return True

def can_move(entities: list[Entity], entity: Entity, portal_positions, grid: list[list[Tile]], dx: int, dy: int) -> bool:
    entity_positions = locate_entities(entities)
    
    x = entity.x
    y = entity.y

    new_x = x + dx
    new_y = y + dy

    if (new_x, new_y) in portal_positions:
        new_pos = get_portal_spawn_pos(grid, new_x, new_y, dx, dy, portal_positions)
        new_x = new_pos[0]
        new_y = new_pos[1]

    if out_of_bounds(grid, new_x, new_y):
        return False
    if new_tile_solid(grid, new_x, new_y):
        return False
    if not can_push(grid, entity_positions, portal_positions, x, y, dx, dy):
        return False
    return True

def can_push(grid, entity_positions, portal_positions, x, y, dx, dy):
    new_entity_x = x + dx
    new_entity_y = y + dy
    if (new_entity_x, new_entity_y) in entity_positions or (new_entity_x, new_entity_y) in portal_positions:
        pushed_entity_new_x = x + (2 * dx)
        pushed_entity_new_y = y + (2 * dy)
        
        # push box into portal
        if (pushed_entity_new_x, pushed_entity_new_y) in portal_positions:
            p1x = pushed_entity_new_x
            p1y = pushed_entity_new_y
            new_pos = get_portal_spawn_pos(grid, p1x, p1y, dx, dy, portal_positions)
            pushed_entity_new_x = new_pos[0]
            pushed_entity_new_y = new_pos[1]

        # box at portal spawn pos
        if (new_entity_x, new_entity_y) in portal_positions:
            p1x = new_entity_x
            p1y = new_entity_y
            new_pos = get_portal_spawn_pos(grid, p1x, p1y, dx, dy, portal_positions)
            if (new_pos[0], new_pos[1]) in entity_positions:    
                print("C")
                pushed_entity_new_x = new_pos[0] + dx
                pushed_entity_new_y = new_pos[1] + dy
            else:
                return True

        if (pushed_entity_new_x, pushed_entity_new_y) in entity_positions:
            return False
        if out_of_bounds(grid, pushed_entity_new_x, pushed_entity_new_y):
            return False
        if new_tile_solid(grid, pushed_entity_new_x, pushed_entity_new_y):
            return False

    return True

def push(grid, entities, entity_positions, portal_positions, x, y, dx, dy, sfx):
    pos = (x + dx, y + dy)
    if pos in entity_positions:
        for i in range(len(entities)):
            if entities[i].pos == pos:
                portal_pos = (entities[i].x + dx, entities[i].y + dy)
                if portal_pos in portal_positions:
                    p1x = portal_pos[0]
                    p1y = portal_pos[1]
                    new_pos = get_portal_spawn_pos(grid, p1x, p1y, dx, dy, portal_positions)
                    new_x = new_pos[0]
                    new_y = new_pos[1]
                    play_sound(teleport_sound, sfx)
                    entities[i].set_pos(new_x, new_y)

                else:
                    entities[i].move(dx, dy)
def teleport(grid, entities, entity, entity_positions, portal_positions, dx, dy, sfx):
    if entity.pos in portal_positions:  
        p1x = entity.x
        p1y = entity.y
        new_pos = get_portal_spawn_pos(grid, p1x, p1y, dx, dy, portal_positions)
        new_x = new_pos[0]
        new_y = new_pos[1]
        if (new_x, new_y) in entity_positions:
            for i in range(len(entities)):
                if entities[i].pos == (new_x, new_y):
                    entities[i].move(dx,dy)
        play_sound(teleport_sound, sfx)
        entity.set_pos(new_x, new_y)
        
def get_portal_spawn_pos(grid, p1x, p1y, dx, dy, portal_positions):
    new_x = p1x + dx
    new_y = p1y + dy
    tile = grid[p1y][p1x]
    tag = tile.tag
    for portal in portal_positions:
        if portal != (p1x, p1y):
            p2x = portal[0]
            p2y = portal[1]
            if grid[p2y][p2x].tag == tag:
                new_x = p2x + dx
                new_y = p2y + dy
    return (new_x, new_y)