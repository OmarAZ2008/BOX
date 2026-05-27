from scripts.tile import Tile

def locate(grid: list[list[Tile]], tile_type: str) -> list[tuple]:
    positions = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tile = grid[i][j]
            if tile.tile_type == tile_type:
                positions.append((j,i))
    return positions