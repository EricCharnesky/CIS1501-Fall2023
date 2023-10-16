
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
    print("\n-----\n".join("|".join(row) for row in board ))
    #print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    #print("-----")
    #print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    #print("-----")
    #print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def make_move(board, current_player):
    print_board(board)
    row = int(input("Enter the row # 0 - 2"))
    column = int(input("enter the column # 0 - 2"))
    while row < 0 or row > 2 or column < 0 or column > 2 or board[row][column] != " ":
        print("invalid move")
        row = int(input("Enter the row # 0 - 2"))
        column = int(input("enter the column # 0 - 2"))
    board[row][column] = current_player



board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

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

#board = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] ]




multiplication_table = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # index 0 row
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], # index 1 row
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30] # index 2 row
]

print("3 x 7 is ", multiplication_table[2][6]) # row 2, column 6

multiplication_table = []

for row in range(1, 11): # gets values 1 - 10
    multiplication_table.append([]) # adds an empty list for the row
    for column in range(1, 11):
        multiplication_table[row-1].append(row * column)

for row in multiplication_table:
    print(row)

first_value = int(input("Enter the first multiple"))
second_value = int(input("Enter the second multiple"))

print(first_value, "x", second_value, "is", multiplication_table[first_value-1][second_value-1])


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# won't change the values in the list
# value is a copy of the value in the list, not the original
for value in my_list:
    value += 10
    print(value)

print(my_list)

# changes the values in the list
for index in range(len(my_list)):
    my_list[index] += 10
    print(my_list[index])

print(my_list)

# slicing - makes a copy
middle_three_values = my_list[3:6]
print(middle_three_values)
for index in range(len(middle_three_values)):
    middle_three_values[index] -= 10

print(middle_three_values)
print(my_list)

# takes a slice from beginning to end
copy_of_my_list = my_list[:]


new_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# you shouldn't modify a list as you iterate over it
#for index in range(len(new_list)):
#    if new_list[index] % 2 == 0:
#        new_list.remove(new_list[index])

#print(new_list)
# doesn't crash, but skips values as we iterate
for value in new_list:
    if value % 2 != 0:
        new_list.remove(value)

# loop over a copy that doesn't change as we change the original
for value in new_list[:]:
    if value % 2 != 0:
        new_list.remove(value)

print(new_list)

new_list.sort()

print(new_list)

if "":
    print("empty is true")
else:
    print("empty is false")