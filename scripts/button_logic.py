from scripts.tile import Tile

def get_pressed_buttons(button_positions: list[tuple], entity_positions: list[tuple]):
    buttons = []
    for button_pos in button_positions:
        if button_pos in entity_positions:
            buttons.append(button_pos)
    return buttons

def get_pressed_button_tags(grid, pressed_button_positions) -> list[str]:
    tags: list[str] = []
    for button in pressed_button_positions:
        x = button[0]
        y = button[1]
        tile = grid[y][x]
        tag = tile.tag
        tags.append(tag)
    return tags

def update_gate_state(grid, button_positions, gate_positions, entity_positions):
    pressed_button_positions = get_pressed_buttons(button_positions, entity_positions)
    pressed_tags = get_pressed_button_tags(grid, pressed_button_positions)
    for gate in gate_positions:
        x = gate[0]
        y = gate[1]
        tile = grid[y][x]
        tag = tile.tag
        if tag in pressed_tags:
            tile.solid = False
            tile.color = (0,0,0)
        else:
            tile.solid = True
            tile.color = (120,120,120)


