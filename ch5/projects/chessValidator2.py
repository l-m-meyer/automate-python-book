import sys
from collections import namedtuple

BLACK   = 'b'
WHITE   = 'w'

KING    = 'king'
QUEEN   = 'queen'
ROOK    = 'rook'
BISHOP  = 'bishop'
KNIGHT  = 'knight'
PAWN    = 'pawn'

COLOURS = {BLACK, WHITE}
PIECES  = {KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN}

RANKS   = set('12345678')
COLUMNS = set('abcdefgh')

VALID_COUNTS = {
    PAWN:   range(0, 9),
    KNIGHT: range(0, 3),
    BISHOP: range(0, 3),
    ROOK:   range(0, 3),
    QUEEN:  range(0, 10),    # pawns can become queens
    KING:   range(0, 2)
}

INPUT_BOARDS = {
    'orig': {
        '1h': 'bking',
        '6c': 'wqueen',
        '2g': 'bbishop',
        '5h': 'bqueen',
        '3e': 'wking',
        '3f': 'bbishop',
    },
    'bad1': {
        '9h': 'bking',
        '9x': 'wking',
    },
    'bad2': {
        '1h': 'bking',
        '3c': 'bking',
        '3f': 'wbishop',
        '7g': 'wbishop',
        '8h': 'wbishop'
    },
    'bad3': {
        '1h': 'wbishop',
        '6c': 'wqueen',
        '2g': 'wbishop',
        '5h': 'wqueen',
        '3e': 'wking',
        '3f': 'wrook',
        '3g': 'wrook',
        '5a': 'wknight',
        '5b': 'wknight',
        '5c': 'wknight',
        '7a': 'wpawn',
        '7b': 'wpawn',
        '7c': 'wpawn',
        '7d': 'wpawn',
        '7e': 'wpawn',
        '7g': 'wpawn',
        '7h': 'wpawn',
    }
}

ParsedCell = namedtuple('ParsedCell', 'cell colour_piece rank column colour piece')

def main(args):
    board = parse_input_board(INPUT_BOARDS[args[0]])
    errors = check_board(board)
    if errors:
        for e in errors:
            print(e)
    else:
        print('OK')


def parse_input_board(input_board):
    return tuple(
        ParsedCell(
            cell,
            colour_piece,
            cell[0:1],
            cell[1:],
            colour_piece[0:1],
            colour_piece[1:],
        )
        for cell, colour_piece in input_board.items()
    )


def check_board(board):
    errors = []
    counts = {}
    for pcell in board:
        # get colour count in dict counts
        if pcell.colour not in counts:
            counts[pcell.colour] = 1
        else:
            counts[pcell.colour] += 1

        # get colour_piece count in dict counts
        if pcell.colour_piece not in counts: 
            counts[pcell.colour_piece] = 1
        else:
            counts[pcell.colour_piece] += 1

        # Check for errors    
        if pcell.rank not in RANKS:
            msg = emsg('Invalid rank', pcell.cell)
            errors.append(msg)

        if pcell.column not in COLUMNS:
            msg = emsg('Invalid column', pcell.cell)
            errors.append(msg)

        if pcell.colour not in COLOURS:
            msg = emsg('Invalid colour', pcell.cell)
            errors.append(msg)

        if pcell.piece not in PIECES:
            msg = emsg('Invalid piece type', pcell.cell)
            errors.append(msg)

        if counts[pcell.colour_piece] not in VALID_COUNTS[pcell.piece]:
            msg = emsg('Invalid number of piece type', pcell.colour_piece)
            errors.append(msg)
        
        if counts[pcell.colour] > 16:
            msg = emsg('More than 16 pieces for colour', pcell.colour)
            errors.append(msg)
        
    return errors


def emsg(msg, item):
    return f'{msg}: {item}'


if __name__ == '__main__':
    main(sys.argv[1:])  # choose input board by key name