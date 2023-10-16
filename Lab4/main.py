def did_someone_win_horizontally(board):
    for row in board:
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return True
    return False


def did_someone_win_vertically(board):
    for column in range(3): # values 0-2
        if board[0][column] != " " and \
            board[0][column] == board[1][column] == board[2][column]:
            return True
    return False # didn't find a matching vertical



def did_someone_win_diagonally(board):
    return board[1][1] != " " and ( ( board[0][0] == board[1][1] == board[2][2] ) \
        or ( board[0][2] == board[1][1] == board[2][0] ) )


def did_someone_win(board):
    return did_someone_win_horizontally(board) or \
        did_someone_win_vertically(board) or \
        did_someone_win_diagonally(board)


def is_cats_game(board):
    for row in board:
        if " " in row:
            return False
    return True # didn't find a space, must be true


def is_game_over(board):
    return did_someone_win(board) or is_cats_game(board)

def print_board(board):
    for row in board:
        print(row)

def make_move(board, current_player):
    print_board(board)
    column = int(input("enter the column # 0 - 6"))
    while column < 0 or column > 6 or board[0][column] != " ":
        print("invalid move")
        column = int(input("enter the column # 0 - 2"))

    # find first open row starting at 5 going up
    for row_index in range(5, -1, -1): # gives 5, 4, 3, 2, 1, 0
        if board[row_index][column] == " ":
            board[row_index][column] = current_player
            break




board = []

for row in range(6):
    board.append([])
    for column in range(7):
        board.append(' ')

current_player = 'X'

while not is_game_over(board):
    make_move(board, current_player)
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
print("Game over!")
print_board(board)
print()