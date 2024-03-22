import random

board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def print_board(board):
    for row in board:
        print("".join(row))

def set_mode():
    valid_mode = False
    while not valid_mode:
        mode = input("Choose game mode:\n1.One Player\n2.Two Player\nEnter: ")
        if mode.isdigit():
            mode = int(mode)
            if mode in [1,2]:
                valid_mode = True
            else:
                print("Invalid number. Enter 1 or 2")
        else:
            print("Invalid input. Enter number")
    return mode

def player_move(player, board):
    symbol = "X" if player == "Player 1" else "O"
    valid_move = False
    while not valid_move:
        move = input(f"{player}'s turn {symbol}: Enter your move 1-9: ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                row = (move - 1) //3
                col = (move - 1) %3
                if board[row][col] == "-":
                    valid_move = True
                else:
                    print("That position is taken. Try again")
            else:
                print("Your move is out of range. Try again")
        else:
            print("Invalid input. Enter number")
    return row,col

def computer_move(board):
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == "-":
            return row,col

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '-':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]

    return None

def full_board(board):
    for row in board:
        if '-' in row:
            return False
    return True

def play():
    mode = set_mode()
    turn = "X"
    while True:
        print_board(board)
        if mode == 1:
            if turn == "X":
                row,col = player_move("Player 1", board)
            else:
                row,col = computer_move(board)
                print("\nComputer's move")
        else:
            if turn == "X":
                row,col = player_move("Player 1", board)
            else:
                row,col = player_move("Player 2", board)
        board[row][col] = turn
        winner = check_winner(board)
        if winner:
            print_board(board)
            if mode == 1 and turn == "X":
                print("\nYou win!")
            elif mode == 1  and turn == "O":
                print("\nComputer wins!")
            elif mode == 2 and turn == "X":
                print("\nPlayer 1 wins!")
            else:
                print("\nPlayer 2 wins!")
            break
        if full_board(board):
            print_board(board)
            print("\nIt's a draw.")
            break
        turn = "O" if turn == "X" else "X"
play()
