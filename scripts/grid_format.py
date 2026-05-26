from scripts.tile import Tile

tiles = {
    "air":{"color":(255,255,255), "solid":False},
    "wall":{"color":(120,120,120), "solid":True}
}


def format_grid(level: list[list[int]]) -> list[list[Tile]]:
    grid = []
    for i in range(len(level)):
        row = []
        for j in range(len(level[i])):
            tile_type = level[i][j]
            if tile_type not in tiles:
                tile_type = "air"
            color = tiles[tile_type]["color"]
            solid = tiles[tile_type]["solid"] 
            row.append(Tile(tile_type, color, solid))
        grid.append(row)
    return grid