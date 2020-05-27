# Author: Patrick O'Donnell


def create_board():
    try:
        num_row = int(
            input("Please input the number of rows for the board:  "))
        num_col = int(
            input("Please input the number of columns for the board:  "))

        # board must be at least 3x3 and rows must equal columns
        if num_row == num_col and num_row + num_col >= 6:
            board = [["_" for row in range(num_row)] for col in range(num_col)]
            return board
        else:
            print("Incorrect dimensions for TicTacToe.")
            print("Tip: Dimensions should be equal to or greater than 3x3",
                  "and the rows and columns must equal each other.")
            return create_board()
    except ValueError:
        print("Incorrect input, enter an integer.")
        return create_board()


def assign_players():
    try:
        players = input("Enter a one character symbol (not '_') for player 1 "
                        "and 2 using the format [P1, P2]:  ")
        player_1 = players[:players.index(",")].strip()
        player_2 = players[players.index(",") + 1:].strip()

        if len(player_1) != 1 or len(player_2) != 1:
            print("Use one character for each player.")
            raise ValueError
        elif player_1 == "_" or player_2 == "_":
            print("Do not use '_'.")
            raise ValueError
        elif player_1 == player_2:
            print("Players must be different characters!")
            raise ValueError

        return (player_1, player_2)
    except ValueError:
        print("Incorect input.")
        return assign_players()


def print_board(board):
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            print(board[row_idx][col_idx], end=" ")
        print("")


def take_inputs(board, player):
    try:
        pos = input(f"{player}, please place your marker using a [Row, Column]"
                    " format:  ")
        row = int(pos[0:pos.index(",")])
        col = int(pos[pos.index(",") + 1:])

        if board[row][col] != "_":
            print("That index has already been used, try again.")
            take_inputs(board, player)
        elif row < 0 or col < 0:
            print("Use positive integers.")
            raise ValueError
        board[row][col] = player
    except ValueError:
        print("Incorrect input, please use the format [Row, Column].")
        return take_inputs(board, player)
    except IndexError:
        print("That position is out of range, try again.")
        return take_inputs(board, player)


def is_finished(board):
    # Checking for diagonal win
    left_diagonal_line = []
    right_diagonal_line = []
    for row_idx, row in enumerate(board[0]):
        left_diagonal_line.append(board[row_idx][row_idx])
        right_diagonal_line.append(board[row_idx][len(row) - row_idx - 1])

    if len(set(left_diagonal_line)) == 1 and "_" not in left_diagonal_line:
        return True, left_diagonal_line[0]
    if len(set(right_diagonal_line)) == 1 and "_" not in right_diagonal_line:
        return True, left_diagonal_line[0]

    # Checking for row win
    for row_idx, row in enumerate(board):
        if len(set(row)) == 1 and "_" not in row:
            print("row win")
            return True, row[0]

    # Checking for column win
    current_col = []
    for i in range(len(board[0])):  # create current_col for each col in board
        for row_idx, row in enumerate(board):
            for col in row:
                current_col.append(board[row_idx][i])
        if len(set(current_col)) == 1 and "_" not in current_col:
            return True, col[0]
        current_col.clear()

    # Checking for empty space. If empty space, keep playing
    for row in board:
        for col in row:
            if col == "_":
                return False
    return "Draw"


def play_game():
    game_board = create_board()
    # used to swtich turns and record player and symbols
    players = list(assign_players())

    while is_finished(game_board) is False:
        print_board(game_board)
        take_inputs(game_board, players[0])
        if is_finished(game_board):
            print_board(game_board)
            print(f"{players[0]} wins!")
        elif is_finished(game_board) == "Draw":
            print("Draw!")
        players.reverse()  # switching turns for players


play_game()
