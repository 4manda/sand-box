from random import randint

board = []

for x in range(5):
    board.append(["-"] * 5)

def print_board(board):
    print(" ".join([" ", "0", "1", "2", "3", "4"]))
    column_num = 0
    for row in board:
        print(str(column_num) + " " + " ".join(row))
        column_num += 1

def random_num(board):
    return randint(0, len(board) - 1)

def createShips(number_ships):
    ships = []
    for x in range(number_ships):
        new = [random_num(board), random_num(board)]
        while new in ships:
            new = [random_num(board), random_num(board)]
        ships.append(new)
    return ships

# def playBattleship(turns, ships)
print("Let's play Battleship!")
print_board(board)

#turns = 15
#number_ships = 3
number_ships = int(input("How many ships? "))
while number_ships < 1 or number_ships > 25:
    if number_ships < 1:
        number_ships = int(input("You have to have some ships! How many ships? "))
    if number_ships > 25:
        number_ships = int(input("There are more ships than space in the ocean! How many ships? "))
turns = int(input("How many turns? "))
while turns < number_ships:
    turns = int(input("You gave yourself less turns than number of ships. Give yourself a fighting chance! How many turns? "))
ships = createShips(number_ships)
print(ships)
ships_sunk = 0

for turn in range(turns):
    print("Turn %s out of %s" % (turn + 1, turns))
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    guess = [guess_row, guess_col]

    if guess in ships:
        if number_ships == ships_sunk + 1:
            board[guess_row][guess_col] = "O"
            print_board(board)
            print("Congratulations! You sunk all %s battleship(s). You Win!" % number_ships)
            break
        else:
            ships[ships.index(guess)] = "hit"
            board[guess_row][guess_col] = "O"
            ships_sunk += 1
            print_board(board)
            print("Congrats! You sunk a battleship. %s to go!" % (number_ships - ships_sunk))
    else:
        if guess_row not in range(0, 5) or guess_col not in range(0, 5):
            print_board(board)
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] != "-":
            print_board(board)
            print("You guessed that one already.")
        else:
            board[guess_row][guess_col] = "X"
            print_board(board)
            print("You hit nada!")
    if turn == turns - 1:
        print("Game Over. You ran out of turns and had %s more battleships to hit :(" % (number_ships - ships_sunk))
