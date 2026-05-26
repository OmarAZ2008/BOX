from scripts.entities import Entity
from scripts.tile import Tile

def can_move(entity: Entity, grid: list[list[Tile]], dx: int, dy: int) -> bool:
    x = entity.x
    y = entity.y
    rows = len(grid)
    cols = len(grid[0])
    if x + dx < 0 or x + dx >= cols:
        return False
    if y + dy < 0 or y + dy >= rows:
        return False
    tile = grid[y+dy][x+dx]
    if tile.solid:
        return False
    return True