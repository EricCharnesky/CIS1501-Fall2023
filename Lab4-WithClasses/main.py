class Connect4:

    def __init__(self):
        self._board = []

        for row in range(6):
            self._board.append([])
            for column in range(7):
                self._board[row].append(' ')
        self._current_player = "X"

    def get_current_player(self):
        return self._current_player

    def _did_someone_win_horizontally(self):
        for row in self._board:
            for column_index in range(4): # 0, 1, 2, 3
                if (row[column_index] != ' ' and row[column_index] == row[column_index+1] \
                        == row[column_index+2] == row[column_index+3]):
                    return True
        return False

    def _did_someone_win_vertically(self):
        for column_index in range(7): # values 0-6
            for row_index in range(3): # 0, 1, 2
                if self._board[row_index][column_index] != " " and \
                    self._board[row_index][column_index] == self._board[row_index+1][column_index] \
                    == self._board[row_index+2][column_index] == self._board[row_index+3][column_index]:
                    return True
        return False # didn't find a matching vertical

    def _did_someone_win_diagonally_up(self):
        for row_index in range(3,6): # bottom three rows 3, 4, 5
            for column_index in range(0, 4): # first 4 columns , 0, 1, 2, 3
                if (self._board[row_index][column_index] != " " and \
                    self._board[row_index][column_index] == self._board[row_index - 1][column_index + 1] ==
                        self._board[row_index - 2][column_index + 2] == self._board[row_index - 3][column_index + 3]):
                    return True
        return False

    def _did_someone_win_diagonally_down(self):
        for row_index in range(0, 3): # top three rows 0, 1, 2
            for column_index in range(0, 4): # first 4 columns , 0, 1, 2, 3
                if (self._board[row_index][column_index] != " " and \
                    self._board[row_index][column_index] == self._board[row_index + 1][column_index + 1] ==
                        self._board[row_index + 2][column_index + 2] == self._board[row_index + 3][column_index + 3]):
                    return True
        return False

    def _did_someone_win(self):
        return self._did_someone_win_horizontally() or \
            self._did_someone_win_vertically() or \
            self._did_someone_win_diagonally_up() or \
            self._did_someone_win_diagonally_down()

    def _is_tied(self):
        for row in self._board:
            if " " in row:
                return False
        return True # didn't find a space, must be true

    def is_game_over(self):
        return self._did_someone_win() or self._is_tied()

    # represents instance of the class as a string
    def __str__(self):
        return "\n".join(str(row) for row in self._board)


    def make_move(self, column):
        if column < 0 or column > 6 or self._board[0][column] != " ":
            return False

        # find first open row starting at 5 going up
        for row_index in [5, 4, 3, 2, 1, 0]: # range(5, -1, -1): # gives 5, 4, 3, 2, 1, 0
            if self._board[row_index][column] == " ":
                self._board[row_index][column] = self._current_player
                break

        if self._current_player == "X":
            self._current_player = "O"
        else:
            self._current_player = "X"
        return True


game = Connect4()

while not game.is_game_over():
    print(game) # automatically calls the __str__ function
    print(game.get_current_player() + "'s turn")
    column = int(input("Enter a column # to drop your piece in"))
    if not game.make_move(column):
        print("Invalid move")

print(game)
print("Game over!")