import secrets

def throw_dices():
    rows = 5
    cols = 5
    dice_throws = []
    dices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S',
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sides = range(1, 7)
    dirs = range(0, 4)
    while dices:
        dice = secrets.choice(dices)
        side = secrets.choice(sides)
        dir = secrets.choice(dirs)
        dice_throws.append((dice, side, dir))
        dices.remove(dice)
    grid = []
    for row in range(rows):
        grid.append([None] * cols)
    row = 0
    col = 0
    for dice in dice_throws:
        grid[row][col] = dice
        col += 1
        if col > cols - 1:
            row += 1
            col = 0
    dirs = ["U", "D", "L", "R"]
    output = []
    for row in range(rows):
        to_display = []
        for dice in grid[row]:
            to_display.append(dice[0] + str(dice[1]) + dirs[dice[2]])
        output.append(" ".join(to_display))
    return "\n".join(output)

print(throw_dices())
