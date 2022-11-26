import random
import re

WIDTH, HEIGHT, PROBABILITY = 10, 10, 80
grid = []
bomb_num, wrong_bomb = 0, 0
cell_icons = {
    "hidden": "  ",
    "flagged": "\"|",
    "bomb": "##",
    "value": ["  ", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8"]
}

index = lambda x, y : x + y * WIDTH

class Cell:
    def __init__(self, is_bomb):
        self.is_bomb = is_bomb
        self.revealed = False
        self.flagged = False
        self.neigh_bombs = 0

for i in range(WIDTH*HEIGHT):
    if random.randint(1,100) >= PROBABILITY:
        grid.append(Cell(True))
        bomb_num += 1
    else:
        grid.append(Cell(False))

for y in range(HEIGHT):
    for x in range(WIDTH):
        if grid[index(x,y)].is_bomb:
            continue
        for y2 in range(-1,2):
            for x2 in range(-1,2):
                if x + x2 >= 0 and x + x2 < WIDTH and y + y2 >= 0 and y + y2 < HEIGHT:
                    if grid[index(x + x2, y + y2)].is_bomb:
                        grid[index(x,y)].neigh_bombs += 1

def get_char(cell):
    if cell.flagged:
        return cell_icons["flagged"]
    if not cell.revealed:
        return cell_icons["hidden"]
    if cell.is_bomb:
        return cell_icons["bomb"]
    return cell_icons["value"][cell.neigh_bombs]

def show_grid():
    print(f"---[{bomb_num}]---")
    for y in range(-1, HEIGHT):
        for x in range(-1, WIDTH):
            if y == -1 and x == -1:
                print(f"[  ]", end=" ")
            elif y == -1:
                print(f"[{x + 1: >2}]", end=" ")
            elif x == -1:
                print(f"[{y + 1: >2}]", end=" ")
            else:
                print(f"({get_char(grid[index(x,y)])})", end=" ")
        print()

def reveal_cell(x, y):
    if grid[index(x,y)].is_bomb:
        return 'L'
    if grid[index(x,y)].revealed:
        return ' '

    grid[index(x,y)].revealed = True
    if grid[index(x,y)].neigh_bombs > 0:
        return ' '

    for y2 in range(-1,2):
        for x2 in range(-1,2):
            if x + x2 >= 0 and x + x2 < WIDTH and y + y2 >= 0 and y + y2 < HEIGHT and not (x2 == 0 and y2 == 0):
                reveal_cell(x + x2, y + y2)
    return ' '

if __name__ == '__main__':
    while True:
        show_grid()
        choice = input("Select choice ([ reveal(r) / toggle flag(f) ] x,y): ")
        r_or_f = re.split(r"\s", choice)[0]
        choiceX, choiceY = re.split(r",", re.split(r"\s", choice)[1])
        choiceX, choiceY = int(choiceX) - 1, int(choiceY) - 1
        if r_or_f == "r" or r_or_f == "reveal":
            if reveal_cell(choiceX, choiceY) == 'L':
                print("You hit a bomb!")
                break
        elif r_or_f == "f" or r_or_f == "flag":
            cell_index = index(choiceX, choiceY)
            grid[cell_index].flagged = not grid[cell_index].flagged
            if grid[cell_index].flagged:
                if grid[cell_index].is_bomb:
                    bomb_num -= 1
                else:
                    wrong_bomb += 1
            else:
                if grid[cell_index].is_bomb:
                    bomb_num += 1
                else:
                    wrong_bomb -= 1
            if bomb_num == 0 and wrong_bomb == 0:
                print("You won!")
                break
    for i in grid:
        i.revealed = True
    show_grid()
