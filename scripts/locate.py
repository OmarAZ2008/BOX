from scripts.tile import Tile
from scripts.entities import Entity

def locate_tiles(grid: list[list[Tile]], tile_type: str) -> list[tuple]:
    positions = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tile = grid[i][j]
            grid_tile_type = tile.tile_type
            if ":" in grid_tile_type:
                pos = grid_tile_type.find(":")
                grid_tile_type = grid_tile_type[0:pos]
            if grid_tile_type == tile_type:
                positions.append((j,i))
    return positions

def locate_entities(entities: list[Entity]) -> list[tuple]:
    positions = []
    for entity in entities:
        positions.append(entity.pos)
    return positions