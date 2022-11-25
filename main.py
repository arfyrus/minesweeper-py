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

for y in range(HEIGHT):
    for x in range(WIDTH):
        if grid[index(x,y)].is_bomb:
            continue
        for y2 in range(-1,2):
            for x2 in range(-1,2):
                if x + x2 >= 0 and x + x2 < WIDTH and y + y2 >= 0 and y + y2 < HEIGHT and not (x == x2 and y == y2):
                    if grid[index(x + x2, y + y2)].is_bomb:
                        grid[index(x,y)].neigh_bombs += 1

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
