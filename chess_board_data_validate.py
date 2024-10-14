board = {'2a': 'wP', '1a': 'wR', '1b': 'wQ', '1f': 'wN', '3a': 'wB',
         '5a': 'wK', '7d': 'wB', '4h': 'wN', '2d': 'wP', '7a': 'bR', '7c': 'bQ', '7e': 'bP',
         '7h': 'bP', '8a': 'bN', '8d': 'bK', '8f': 'bP', '6g': 'bN', '5d': 'bP', '5g': 'bP',
         '8h': 'bB', '2h': 'bN', '3h': 'bN'}


black_pieces = 0
white_pieces = 0
total_pieces = 0
white_king = 0
black_king = 0
white_queen = 0
black_queen = 0
white_rook = 0
black_rook = 0
white_knight = 0
black_knight = 0
white_pawn = 0
black_pawn = 0

for key, value in board.items():
    if value[0].lower() == 'w':
        white_pieces += 1
        if value[1].upper() == 'P':
            white_pawn += 1
        elif value[1].upper() == 'K':
            white_king += 1
        elif value[1].upper() == 'N':
            white_knight += 1
        elif value[1].upper() == 'R':
            white_rook += 1
        elif value[1].upper() == 'Q':
            white_queen += 1

    else:
        black_pieces += 1
        if value[1].upper() == 'P':
            black_pawn += 1
        elif value[1].upper() == 'K':
            black_king += 1
        elif value[1].upper() == 'N':
            black_knight += 1
        elif value[1].upper() == 'R':
            black_rook += 1
        elif value[1].upper() == 'Q':
            black_queen += 1

    total_pieces += 1

if black_pieces <= 16:
    print('Valid: Total black pieces - {} black pieces'.format(black_pieces))
else:
    print('Invalid: Total black pieces - {} black pieces'.format(black_pieces))

if white_pieces <= 16:
    print('Valid: Total white pieces - {} white pieces'.format(white_pieces))
else:
    print('Invalid: Total white pieces - {} white pieces'.format(white_pieces))

if total_pieces <= 32:
    print('Valid: Total pieces - {} total pieces'.format(total_pieces))
else:
    print('Invalid: Total pieces - {} total pieces'.format(total_pieces))
print()
if white_king == 1 and black_king == 1:
    print('Valid: Kings - One of each color.')
else:
    print('Invalid: Kings - One of each color.')
print()
if white_queen <= 2:
    print('Valid: Total white queen pieces - {} total white queen pieces'.format(white_queen))
else:
    print('Invalid: Total white queen pieces - {} total white queen pieces'.format(white_queen))

if black_queen <= 2:
    print('Valid: Total black queen pieces - {} total black queen pieces'.format(black_queen))
else:
    print('Invalid: Total black queen pieces - {} total black queen pieces'.format(black_queen))

if black_queen + white_queen <= 4:
    print('Valid: Total queen pieces - {} total queen pieces'.format(black_queen + white_queen))
else:
    print('Invalid: Total queen pieces - {} total queen pieces'.format(black_queen + white_queen))
print()
if black_rook <= 2:
    print('Valid: Total black rook pieces - {} total black rook pieces'.format(black_rook))
else:
    print('Invalid: Total black rook pieces - {} total black rook pieces'.format(black_rook))

if white_rook <= 2:
    print('Valid: Total white rook pieces - {} total white rook pieces'.format(white_rook))
else:
    print('Invalid: Total white rook pieces - {} total white rook pieces'.format(white_rook))

if white_rook + black_rook <= 4:
    print('Valid: Total rook pieces - {} total rook pieces'.format(white_rook + black_rook))
else:
    print('Invalid: Total rook pieces - {} total rook pieces'.format(white_rook + black_rook))
print()
if white_knight <= 2:
    print('Valid: Total white knight pieces - {} total white knight pieces'.format(white_knight))
else:
    print('Invalid: Total white knight pieces - {} total white knight pieces'.format(white_knight))

if black_knight <= 2:
    print('Valid: Total black knight pieces - {} total black knight pieces'.format(black_knight))
else:
    print('Invalid: Total black knight pieces - {} total black knight pieces'.format(black_knight))

if black_knight + white_knight <= 2:
    print('Valid: Total knight pieces - {} total knight pieces'.format(black_knight + white_knight))
else:
    print('Invalid: Total knight pieces - {} total knight pieces'.format(black_knight + white_knight))
print()
if black_pawn <= 8:
    print('Valid: Total black pawn pieces - {} total black pawn pieces'.format(black_pawn))
else:
    print('Invalid: Total black pawn pieces - {} total black pawn pieces'.format(black_pawn))

if white_pawn <= 8:
    print('Valid: Total white pawn pieces - {} total white pawn pieces'.format(white_pawn))
else:
    print('Invalid: Total white pawn pieces - {} total white pawn pieces'.format(white_pawn))

if white_pawn + black_pawn <= 16:
    print('Valid: Total pawn pieces - {} total pawn pieces'.format(white_pawn + black_pawn))
else:
    print('Invalid: Total pawn pieces - {} total pawn pieces'.format(white_pawn + black_pawn))
