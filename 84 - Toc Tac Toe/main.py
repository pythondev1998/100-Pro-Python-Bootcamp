import random

def display_board(board):
    print("-------------")
    print("|", board[7], "|", board[8], "|", board[9], "|")
    print("-------------")
    print("|", board[4], "|", board[5], "|", board[6], "|")
    print("-------------")
    print("|", board[1], "|", board[2], "|", board[3], "|")
    print("-------------")

def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Do you want to be X or O? ").upper()
    return marker

def place_marker(board, marker, position):
    board[position] = marker

def check_winner(board, marker):
    return (
        (board[1] == board[2] == board[3] == marker)
        or (board[4] == board[5] == board[6] == marker)
        or (board[7] == board[8] == board[9] == marker)
        or (board[1] == board[4] == board[7] == marker)
        or (board[2] == board[5] == board[8] == marker)
        or (board[3] == board[6] == board[9] == marker)
        or (board[1] == board[5] == board[9] == marker)
        or (board[3] == board[5] == board[7] == marker)
    )

def is_board_full(board):
    return " " not in board[1:]

def get_computer_move(board, computer_marker):
    available_moves = [pos for pos in range(1, 10) if board[pos] == " "]
    return random.choice(available_moves)

def tic_tac_toe_game():
    board = [" "] * 10
    player_marker = player_input()

    if player_marker == "X":
        computer_marker = "O"
    else:
        computer_marker = "X"

    while True:
        # Player's turn
        display_board(board)
        position = int(input("Choose a position (1-9): "))

        if board[position] == " ":
            place_marker(board, player_marker, position)

            if check_winner(board, player_marker):
                display_board(board)
                print("Congratulations! You've won!")
                break

            if is_board_full(board):
                display_board(board)
                print("It's a draw.")
                break

            # AI's turn
            position = get_computer_move(board, computer_marker)
            place_marker(board, computer_marker, position)

            if check_winner(board, computer_marker):
                display_board(board)
                print("The AI has won. Try again!")
                break

            if is_board_full(board):
                display_board(board)
                print("It's a draw.")
                break

tic_tac_toe_game()
