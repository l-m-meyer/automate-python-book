# my first attempt
def isValidChessBoard(board):
    # Takes a dictionary `board` and returns True if board is valid, False otherwise.

    piecesCount = {'b': 0, 'w': 0}
    pawnCount = {'b': 0, 'w': 0}
    hasKing = {'b': False, 'w': False}
    letterAxis = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    pieceColour = ('b', 'w')
    pieceType = ('pawn', 'knight', 'bishop', 'rook', 'king', 'queen')

    validPieces = isValidMaxPieces(board, piecesCount, pieceType, pieceColour)
    validKings = isValidKings(board, hasKing)
    validPawns = isValidPawns(board, pawnCount)
    validSpaces = isOnValidSpaces(board, letterAxis)
    
    valid_board = validPieces and validKings and validPawns and validSpaces
    print(valid_board)
    return valid_board

def isValidMaxPieces(board, piecesCount, pieceType, pieceColour):
    # Check that each player has <= 16 pieces
    for piece in board.values():
        if isValidPieceName(piece, pieceType, pieceColour):
            color = piece[0]
            piecesCount[color] += 1

    for v in piecesCount.values():
        if v <= 16:
            return True, piecesCount
    return False


def isValidPawns(board, pawns):
    # Check that each player has <= 8 pawns
    for piece in board.values():
        if piece[0] == 'b' and piece[1:] == 'pawn':
            pawns['b'] += 1
        if piece[0] == 'w' and piece[1:] == 'pawn':
            pawns['w'] += 1
    return pawns


def isValidKings(board, kings):
    # Check that each player has one king
    bkingCount = 0
    wkingCount = 0

    if 'bking' in board.values() and bkingCount < 1:
        bkingCount += 1
        kings['b'] = True
    
    if 'wking' in board.values() and wkingCount < 1:
        wkingCount += 1
        kings['w'] = True
    return kings


def isOnValidSpaces(board, axis):
    # Check that all pieces are on a valid space from '1a' to '8h'
    for space in board.keys():
        if space[1] not in axis:
            return False
        if int(space[0]) not in range(1, 9):
            return False
    return True


def isValidPieceName(piece, pieceType, pieceColour):
    # Check that piece names begin with 'w' or 'b' followed by valid piece type
    if piece[0] in pieceColour and piece[1:] in pieceType:
        return True
    return False


def check_board(board):
    # Detect when a bug has resulted in an improper chess board
    return


chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4h': 'wpawn'}

isValidChessBoard(chess_board)