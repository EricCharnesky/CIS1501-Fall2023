def did_someone_win_horizontally(board):
    for row in board:
        for column_index in range(4): # 0, 1, 2, 3
            if (row[column_index] != ' ' and row[column_index] == row[column_index+1] \
                    == row[column_index+2] == row[column_index+3]):
                return True
    return False


def did_someone_win_vertically(board):
    for column_index in range(7): # values 0-6
        for row_index in range(3): # 0, 1, 2
            if board[row_index][column_index] != " " and \
                board[row_index][column_index] == board[row_index+1][column_index] \
                == board[row+2][column_index] == board[row+3][column_index]:
                return True
    return False # didn't find a matching vertical



def did_someone_win_diagonally_up(board):
    for row_index in range(3,6): # bottom three rows 3, 4, 5
        for column_index in range(0, 4): # first 4 columns , 0, 1, 2, 3
            if (board[row_index][column_index] != " " and \
                board[row_index][column_index] == board[row_index - 1][column_index + 1] ==
                    board[row_index - 2][column_index + 2] == board[row_index - 3][column_index + 3]):
                return True
    return False


def did_someone_win_diagonally_down(board):
    for row_index in range(0, 3): # top three rows 0, 1, 2
        for column_index in range(0, 4): # first 4 columns , 0, 1, 2, 3
            if (board[row_index][column_index] != " " and \
                board[row_index][column_index] == board[row_index + 1][column_index + 1] ==
                    board[row_index + 2][column_index + 2] == board[row_index + 3][column_index + 3]):
                return True
    return False


def did_someone_win(board):
    return did_someone_win_horizontally(board) or \
        did_someone_win_vertically(board) or \
        did_someone_win_diagonally_up(board) or \
        did_someone_win_diagonally_down(board)

def is_tied(board):
    for row in board:
        if " " in row:
            return False
    return True # didn't find a space, must be true


def is_game_over(board):
    return did_someone_win(board) or is_tied(board)

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
    for row_index in [5, 4, 3, 2, 1, 0]: # range(5, -1, -1): # gives 5, 4, 3, 2, 1, 0
        if board[row_index][column] == " ":
            board[row_index][column] = current_player
            break




board = []

for row in range(6):
    board.append([])
    for column in range(7):
        board[row].append(' ')

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