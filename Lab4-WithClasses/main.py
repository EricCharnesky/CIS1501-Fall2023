from connect4 import Connect4


game = Connect4()

while not game.is_game_over():
    print(game) # automatically calls the __str__ function
    print(game.get_current_player() + "'s turn")
    column = int(input("Enter a column # to drop your piece in"))
    if not game.make_move(column):
        print("Invalid move")

print(game)
print("Game over!")