import tictactoe_tools

player_win = False
ai_win = False
tie = False
game_grid = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
player_token = ""
ai_token = ""
iteration = 0
err_msg = ""


def player_turn():
    global player_win
    global tie
    player_coordinate = tictactoe_tools.player_placement(game_grid)
    game_grid[player_coordinate[0]][player_coordinate[1]] = player_token
    tictactoe_tools.print_grid(game_grid)
    player_win = tictactoe_tools.check_win(game_grid, player_token)
    tie = tictactoe_tools.check_tie(game_grid)


def ai_turn():
    global ai_win
    global tie
    ai_coordinate = tictactoe_tools.ai_placement(game_grid, ai_token, player_token)
    game_grid[ai_coordinate[0]][ai_coordinate[1]] = ai_token
    ai_win = tictactoe_tools.check_win(game_grid, ai_token)
    tictactoe_tools.print_grid(game_grid)
    tie = tictactoe_tools.check_tie(game_grid)


while not (player_token == "X") and not (player_token == "O"):
    if iteration > 0:
        print("Please enter a valid option.\n")
    player_token = input("Would you like to play as X or O? ").upper()
    if player_token == "X":
        ai_token = "O"
    elif player_token == "O":
        ai_token = "X"
    iteration += 1

tictactoe_tools.print_grid(game_grid)
print("\nX goes first.\n")

# Game loop
while not player_win and not ai_win and not tie:
    if player_token == "X":
        player_turn()
        if not player_win and not tie:
            ai_turn()
    else:
        ai_turn()
        if not ai_win and not tie:
            player_turn()

if player_win:
    print("YOU WIN")
elif ai_win:
    print("YOU LOSE")
else:
    print("TIE")
