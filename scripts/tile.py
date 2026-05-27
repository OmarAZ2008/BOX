class Tile:
    def __init__(self, tile_type: str, color: tuple, solid: bool, tag: str):
        self.tile_type = tile_type
        self.color = color
        self.solid = solid
        self.tag = tag