def is_valid_chess_board(board):
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    white_king = 0
    black_king = 0
    white_pieces = 0
    black_pieces = 0
    white_pawns = 0
    black_pawns = 0

    for position, piece in board.items():
        if len(position) != 2 or position[0] not in 'abcdefgh' or position[1] not in '12345678':
            return False
        
        if piece[0] not in ['w', 'b']:
            return False
        pliece_type = piece[1:]
        if pliece_type not in valid_pieces:
            return False
        
        if piece[0] == 'w':
            white_pieces += 1
            if pliece_type == 'king':
                white_king += 1
            if pliece_type == 'pawn':
                white_pawns += 1
        else:
            black_pieces += 1
            if pliece_type == 'king':
                black_king += 1
            if pliece_type == 'pawn':
                black_pawns += 1
        
        if white_king > 1 or black_king > 1:
            return False
        if white_pieces > 16 or black_pieces > 16:
            return False
        if white_pawns > 8 or black_pawns > 8:
            return False
        
        return True
    