import random

PLAYER_X = 'X'
PLAYER_O = 'O'

BOARD_SIZE = 3
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board():
    print("  1   2   3")
    for i in range(BOARD_SIZE):
        print(f"{chr(65 + i)} {' | '.join(board[i])}")
        if i < BOARD_SIZE - 1:
            print(" ---|---|---")

def is_valid_move(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == ' '

def is_game_over():
    for i in range(BOARD_SIZE):
        if all(cell == PLAYER_X for cell in board[i]):
            return PLAYER_X
        if all(cell == PLAYER_O for cell in board[i]):
            return PLAYER_O
        if all(board[j][i] == PLAYER_X for j in range(BOARD_SIZE)):
            return PLAYER_X
        if all(board[j][i] == PLAYER_O for j in range(BOARD_SIZE)):
            return PLAYER_O
    if all(board[i][i] == PLAYER_X for i in range(BOARD_SIZE)):
        return PLAYER_X
    if all(board[i][i] == PLAYER_O for i in range(BOARD_SIZE)):
        return PLAYER_O
    if all(cell != ' ' for row in board for cell in row):
        return 'DRAW'
    return None

def computer_move():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == ' ':
                board[row][col] = PLAYER_X
                if is_game_over() == PLAYER_X:
                    return row, col
                board[row][col] = ' '

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == ' ':
                board[row][col] = PLAYER_O
                if is_game_over() == PLAYER_O:
                    return row, col
                board[row][col] = ' '

    available_moves = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if board[row][col] == ' ']
    return random.choice(available_moves)

while True:
    print_board()

    while True:
        player_input = input("Enter your move (A1 or B2): ").strip().upper()
        if len(player_input) == 2 and player_input[0] in 'ABC' and player_input[1] in '123':
            row = ord(player_input[0]) - ord('A')
            col = int(player_input[1]) - 1
            if is_valid_move(row, col):
                board[row][col] = PLAYER_O
                break
        print("Invalid move. Try again.")

    result = is_game_over()
    if result == 'DRAW':
        print_board()
        print("It's a tie!")
        break
    elif result:
        print_board()
        print("Player O wins!")
        break

    # Computer's move
    computer_row, computer_col = computer_move()
    board[computer_row][computer_col] = PLAYER_X

    result = is_game_over()
    if result == 'DRAW':
        print_board()
        print("It's a tie!")
        break
    elif result:
        print_board()
        print("Computer X wins!")
        break