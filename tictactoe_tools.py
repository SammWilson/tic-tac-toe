import random
import time


def print_grid(game_grid):
    row_iteration = 0
    for row in game_grid:
        col_iteration = 0
        if not row_iteration == 0:
            print("\n_________________")
        for col in row:
            print(col, end="")
            if not col_iteration == 2:
                print("\t|\t", end="")
            col_iteration += 1
        row_iteration += 1
    print("\n")


def check_tie(game_grid):
    for row in game_grid:
        for col in row:
            if col == "":
                return False
    return True


def player_placement(game_grid):
    iteration = 0
    x_coordinate = -1
    y_coordinate = -1
    err_msg = ""
    while x_coordinate not in range(3) or y_coordinate not in range(3):
        if iteration > 0:
            print(err_msg)
        try:
            x_coordinate = int(input("Which row would you like to place your game piece? (1-3) "))
            y_coordinate = int(input("Which column would you like to place your game piece? (1-3) "))
            x_coordinate -= 1
            y_coordinate -= 1
            iteration += 1
            if not (game_grid[int(x_coordinate)][int(y_coordinate)] == ""):
                err_msg = "\nThat space is occupied. Please enter a valid location.\n"
                x_coordinate = -1
                y_coordinate = -1
        except (ValueError, IndexError) as err:
            err_msg = "\nRow or column must be a number between 1-3. Please enter a valid location.\n"
            iteration += 1
            x_coordinate = -1
            y_coordinate = -1

    return [x_coordinate, y_coordinate]


def ai_placement(game_grid, ai_token, player_token):
    print("Computer is thinking", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")

    # Offense
    coordinate = ai_search(game_grid, ai_token)
    if coordinate is not None:
        return coordinate
    # Defense
    coordinate = ai_search(game_grid, player_token)
    if coordinate is not None:
        return coordinate

    # Default
    coordinate = [random.randint(0, 2), random.randint(0, 2)]
    while not game_grid[coordinate[0]][coordinate[1]] == "":
        coordinate = [random.randint(0, 2), random.randint(0, 2)]
    return coordinate


def ai_search(game_grid, token):
    for row in range(3):
        for col in range(3):
            # row check
            if game_grid[row][col] == token:
                if col - 2 in range(3):
                    if game_grid[row][col - 1] == token:
                        if game_grid[row][col - 2] == "":
                            return [row, col - 2]  # _OO
                    if game_grid[row][col - 2] == token:
                        if game_grid[row][col - 1] == "":
                            return [row, col - 1]  # O_O
                elif col - 1 in range(3):
                    if game_grid[row][col - 1] == token:
                        if game_grid[row][col + 1] == "":
                            return [row, col + 1]  # OO_
            # column check
            if game_grid[row][col] == token:
                if row - 2 in range(3):
                    if game_grid[row - 1][col] == token:
                        if game_grid[row - 2][col] == "":
                            return [row - 2, col]  # _OO
                    if game_grid[row - 2][col] == token:
                        if game_grid[row - 1][col] == "":
                            return [row - 1, col]  # O_O
                elif row - 1 in range(3):
                    if game_grid[row - 1][col] == token:
                        if game_grid[row + 1][col] == "":
                            return [row + 1, col]  # OO_
            # diagonal check
            # top left to bottom right direction
            if game_grid[row][col] == token:
                if row - 2 in range(3) and col - 2 in range(3):
                    if game_grid[row - 1][col - 1] == token:
                        if game_grid[row - 2][col - 2] == "":
                            return [row - 2, col - 2]  # _OO ->
                    if game_grid[row - 2][col - 2] == token:
                        if game_grid[row - 1][col - 1] == "":
                            return [row - 1, col + 1]  # O_O ->
                elif row + 1 in range(3) and col + 1 in range(3):
                    if game_grid[row - 1][col - 1] == token:
                        if game_grid[row + 1][col + 1] == "":
                            return [row + 1, col + 1]  # OO_ ->
                # Top right to bottom left direction
                if row + 2 in range(3) and col - 2 in range(3):
                    if game_grid[row + 1][col - 1] == token:
                        if game_grid[row + 2][col - 2] == "":
                            return [row + 2, col - 2]  # _OO <-
                    if game_grid[row + 2][col - 2] == token:
                        if game_grid[row + 1][col - 1] == "":
                            return [row + 1, col - 1]  # O_O <-
                elif row - 2 in range(3) and col + 2 in range(3):
                    if game_grid[row - 1][col + 1] == token:
                        if game_grid[row - 2][col + 2] == "":
                            return [row - 2, col + 2]  # OO_ <-


def check_win(game_grid, token):
    if game_grid[0][0] == token:
        if game_grid[1][0] == token:
            if game_grid[2][0] == token:
                return True
        elif game_grid[0][1] == token:
            if game_grid[0][2] == token:
                return True
        elif game_grid[1][1] == token:
            if game_grid[2][2] == token:
                return True
    if game_grid[0][1] == token:
        if game_grid[1][1] == token:
            if game_grid[2][1] == token:
                return True
    if game_grid[0][2] == token:
        if game_grid[1][1] == token:
            if game_grid[2][0] == token:
                return True
        elif game_grid[1][2] == token:
            if game_grid[2][2] == token:
                return True
    if game_grid[1][0] == token:
        if game_grid[1][1] == token:
            if game_grid[1][2] == token:
                return True
    if game_grid[2][0] == token:
        if game_grid[2][1] == token:
            if game_grid[2][2] == token:
                return True
    else:
        return False
