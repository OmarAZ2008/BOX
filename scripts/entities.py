class Entity:
    def __init__ (self, x: int, y: int, color: tuple):
        self.x = x
        self.y = y
        self.color = color
    def move(self, dx, dy):
        self.x += dx
        self.y += dy