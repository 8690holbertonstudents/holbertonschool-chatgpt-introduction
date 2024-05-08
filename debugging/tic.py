#!/usr/bin/env python3

def print_board(board):
    """Prints the current state of the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
    print("-" * 5)


def is_winner(board, player):
    """Checks if a player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if (
            all(board[row][col] == player for row in range(3))
            and board[0][col] != " "
        ):
            return True

    # Check diagonals
    if (
        board[0][0] == player and board[1][1] == player
        and board[2][2] == player
        and board[0][0] != " "
    ):
        return True
    if (
        board[0][2] == player
        and board[1][1] == player
        and board[2][0] == player
        and board[0][2] != " "
    ):
        return True

    return False


def is_board_full(board):
    """Checks if all spaces on the board are occupied."""
    return all(all(cell != " " for cell in row) for row in board)


def tic_tac_toe():
    """Main game loop that runs the tic-tac-toe game."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid player input
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2)\
                                 for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2)\
                                 for player " + player + ": "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        # Update board and check winner
        board[row][col] = player
        if is_winner(board, player):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
