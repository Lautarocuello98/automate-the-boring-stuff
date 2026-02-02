the_board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
             'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
             'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

def print_board(board):
    print(f"{board['top-l']}|{board['top-m']}|{board['top-r']}")
    print("-+-+-")
    print(f"{board['mid-l']}|{board['mid-m']}|{board['mid-r']}")
    print("-+-+-")
    print(f"{board['low-l']}|{board['low-m']}|{board['low-r']}")

turn = 'X'
for i in range(9):
    print_board(the_board)
    print(f'turn for {turn}. move on which space? ')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)