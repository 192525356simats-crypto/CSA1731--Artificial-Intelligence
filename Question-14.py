def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")


def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def play_game():
    # Initialize board with position numbers 1-9 for easy reference
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves_made = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while moves_made < 9:
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[choice] in ("X", "O"):
                print("That spot is already taken! Try another.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Place the mark and display updated board
        board[choice] = current_player
        moves_made += 1
        print_board(board)

        # Check for a win
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            return

        # Switch turns
        current_player = "O" if current_player == "X" else "X"

    print("It's a draw!")


if __name__ == "__main__":
    play_game()
