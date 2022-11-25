import random

WIDTH, HEIGHT, PROBABILITY = 10, 10, 80
grid = []
cell_icons = {
    "hidden": " ",
    "flagged": "+",
    "bomb": "#",
    "value": [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
}

index = lambda x, y : x + y * WIDTH

class Cell:
    def __init__(self, is_bomb):
        self.is_bomb = is_bomb
        self.revealed = True
        self.flagged = False
        self.neigh_bombs = 0

for i in range(WIDTH*HEIGHT):
    if random.randint(1,100) >= PROBABILITY:
        grid.append(Cell(True))
    else:
        grid.append(Cell(False))

def get_char(cell):
    if not cell.revealed:
        return cell_icons["hidden"]
    if cell.flagged:
        return cell_icons["flagged"]
    if cell.is_bomb:
        return cell_icons["bomb"]
    return cell_icons["value"][cell.neigh_bombs]

def show_grid():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(f"[{get_char(grid[index(x,y)])}]", end=" ")
        print()

if __name__ == '__main__':
    show_grid()
