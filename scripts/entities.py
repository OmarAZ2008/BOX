class Entity:
    def __init__ (self, entity_type, x: int, y: int, color: tuple):
        self.entity_type = entity_type
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.color = color
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.update_pos()
    def update_pos(self):
        self.pos = (self.x, self.y)