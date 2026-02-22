# Tic-Tac-Toe board represented as a dictionary.
# Each key corresponds to a position on the board.
the_board = {
    'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
    'low-l': ' ', 'low-m': ' ', 'low-r': ' '
}

def print_board(board):
    """Print the current board state in a 3x3 grid format."""
    print(f"{board['top-l']}|{board['top-m']}|{board['top-r']}")
    print("-+-+-")
    print(f"{board['mid-l']}|{board['mid-m']}|{board['mid-r']}")
    print("-+-+-")
    print(f"{board['low-l']}|{board['low-m']}|{board['low-r']}")

# Start with player X
turn = 'X'

# Maximum of 9 moves (3x3 board)
for i in range(9):
    print_board(the_board)

    # Ask current player for their move
    print(f"Turn for {turn}. Move on which space?")
    move = input()

    # Update board state with current player's mark
    the_board[move] = turn

    # Switch turn
    turn = 'O' if turn == 'X' else 'X'

# Final board state after all moves
print_board(the_board)