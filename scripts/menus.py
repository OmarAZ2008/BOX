import pygame

pygame.init()

class Menu:
    def __init__(self, type, options, selected_option):
        self.type = type
        self.options = options
        self.selected_option = selected_option
        self.start = 0
        self.end = len(self.options) - 1
        if self.type != "controls":
            self.options[self.selected_option]["color"] = (255,230,50)
    def move_up(self):
        self.options[self.selected_option]["color"] = (255,255,255)
        self.selected_option -= 1
        if self.selected_option < self.start:
            self.selected_option = self.end
        self.options[self.selected_option]["color"] = (255,230,50)
    def move_down(self):
        self.options[self.selected_option]["color"] = (255,255,255)
        self.selected_option += 1
        if self.selected_option > self.end:
            self.selected_option = self.start
        self.options[self.selected_option]["color"] = (255,230,50)
    def move_right(self, unlocked_levels, max_level):
        option = self.options[self.selected_option]
        level = int(option["text"]) - 1
        new_level = level + 1
        if new_level > max_level:
            new_level = 0
        if new_level in unlocked_levels:
            self.options[new_level]["color"] = (255,230,50)
            self.selected_option = new_level
            self.options[level]["color"] = (255,255,255)
    def move_left(self, unlocked_levels, max_level):
        option = self.options[self.selected_option]
        level = int(option["text"]) - 1
        new_level = level - 1
        if new_level < 0:
            new_level = max_level
        if new_level in unlocked_levels:
            self.options[new_level]["color"] = (255,230,50)
            self.selected_option = new_level
            self.options[level]["color"] = (255,255,255)
    def move_level_up(self, unlocked_levels):
        option = self.options[self.selected_option]
        level = int(option["text"]) - 1
        new_level = level - 5
        if new_level < 0:
            return
        if new_level in unlocked_levels:
            self.options[new_level]["color"] = (255,230,50)
            self.selected_option = new_level
            self.options[level]["color"] = (255,255,255)
    def move_level_down(self, unlocked_levels, max_level):
        option = self.options[self.selected_option]
        level = int(option["text"]) - 1
        new_level = level + 5
        if new_level > max_level:
            return
        if new_level in unlocked_levels:
            self.options[new_level]["color"] = (255,230,50)
            self.selected_option = new_level
            self.options[level]["color"] = (255,255,255)
        

def draw_menu(menu, font_size, screen, WIDTH, HEIGHT):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(0)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    menu_font = pygame.font.SysFont(None, font_size)
    x = 0
    y = 0
    dx = 0
    dy = 32
    if menu.type == "title":
        x = 288
        y = 208
        dy = 64
    elif menu.type == "controls":
        x = 32
        y = 32
        dy = 48
    elif menu.type == "levels":
        x = 64
        y = 64
        dx = 64
        dy = 64
        for option in menu.options:
            text = menu_font.render(option["text"], True, option["color"])
            screen.blit(text, (x,y))
            x += dx
            if x >= 6*dx:
                x = dx
                y += dy
        return
    for option in menu.options:
        text = menu_font.render(option["text"], True, option["color"])
        screen.blit(text, (x,y))
        y += dy
    
