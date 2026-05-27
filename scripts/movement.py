from scripts.entities import Entity
from scripts.tile import Tile
from scripts.locate import locate_entities

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

def can_move(entities: list[Entity], entity: Entity, grid: list[list[Tile]], dx: int, dy: int) -> bool:
    entity_positions = locate_entities(entities)
    
    x = entity.x
    y = entity.y

    new_x = x + dx
    new_y = y + dy

    if out_of_bounds(grid, new_x, new_y):
        return False
    if new_tile_solid(grid, new_x, new_y):
        return False
    if not can_push(grid, entity_positions, x, y, dx, dy):
        return False
    return True

def can_push(grid, entity_positions, x, y, dx, dy):
    new_entity_x = x + dx
    new_entity_y = y + dy
    if (new_entity_x, new_entity_y) in entity_positions:
        pushed_entity_new_x = x + (2 * dx)
        pushed_entity_new_y = y + (2 * dy)
        if (pushed_entity_new_x, pushed_entity_new_y) in entity_positions:
            return False
        if out_of_bounds(grid, pushed_entity_new_x, pushed_entity_new_y):
            return False
        if new_tile_solid(grid, pushed_entity_new_x, pushed_entity_new_y):
            return False
    return True

def push(entities, entity_positions, x, y, dx, dy):
    pos = (x + dx, y + dy)
    if pos in entity_positions:
        for i in range(len(entities)):
            if entities[i].pos == pos:
                entities[i].move(dx, dy)


        
