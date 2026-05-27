from scripts.tile import Tile
from scripts.entities import Entity

tiles = {
    "air":{"color":(0,0,0), "solid":False},
    "wall":{"color":(60,60,60), "solid":True},
    "goal":{"color":(0,200,0), "solid":False}
}

entities = {
    "player":{"color":(0,120,255)},
    "box":{"color":(160,110,60)}
}

def format_level(level: list[list[str]]):
    grid = []
    entity_list = []
    for i in range(len(level)):
        row = []
        for j in range(len(level[i])):
            tile_type = level[i][j]
            if tile_type not in tiles:
                if tile_type in entities:
                    color = entities[tile_type]["color"]
                    entity_list.append(Entity(tile_type, j,i,color))

                tile_type = "air"
            color = tiles[tile_type]["color"]
            solid = tiles[tile_type]["solid"] 
            row.append(Tile(tile_type, color, solid))
        grid.append(row)
    return {"grid":grid, "entities":entity_list}

