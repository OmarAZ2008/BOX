level_paths = [
    "levels/level_1.txt",
    "levels/level_2.txt",
    "levels/level_3.txt",
    "levels/level_4.txt",
    "levels/level_5.txt",
]

# a-m: buttons n-z:portals

symbols = {
# non_tagged
    ".":"air",
    "#":"wall",
    "|":"player",
    "*":"goal",
    "+":"box",   
# button/gate
    "A": "button:A",
    "a": "gate:A",
    "B": "button:B",
    "b": "gate:B",
    "C": "button:C",
    "c": "gate:C",
    "D": "button:D",
    "d": "gate:D",
    "E": "button:E",
    "e": "gate:E",
    "F": "button:F",
    "f": "gate:F",
    "G": "button:G",
    "g": "gate:G",
    "H": "button:H",
    "h": "gate:H",
    "I": "button:I",
    "i": "gate:I",
    "J": "button:J",
    "j": "gate:J",
    "K": "button:K",
    "k": "gate:K",
    "L": "button:L",
    "l": "gate:L",
    "M": "button:M",
    "m": "gate:M",
# portals
    "N": "portal:N",
    "O": "portal:O",
    "P": "portal:P",
    "Q": "portal:Q",
    "R": "portal:R",
    "S": "portal:S",
    "T": "portal:T",
    "U": "portal:U",
    "V": "portal:V",
    "W": "portal:W",
    "X": "portal:X",
    "Y": "portal:Y",
    "Z": "portal:Z",
}

def parse_level(path):
    with open(path) as file:
        lines = [line.strip() for line in file]

    level = []

    for j in range(len(lines)):
        row  = []
        for i in range(len(lines[j])):
            char = lines[i][j]
            if char in symbols:
                row.append(symbols[char])
        level.append(row)

parsed_levels = []
for path in level_paths:
    parsed_levels.append(parse_level(path))
