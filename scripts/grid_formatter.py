from scripts.tile import Tile

tiles = {
    "air":{"color":(0,0,0), "solid":False},
    "wall":{"color":(60,60,60), "solid":True},
    "goal":{"color":(0,200,0), "solid":False}
}


def format_grid(level: list[list[str]]) -> list[list[Tile]]:
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