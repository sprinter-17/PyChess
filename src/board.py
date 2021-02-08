class Board:

    def __init__(self):
        self.pieces = [
                          Piece(Piece.WHITE, Piece.PAWN, (2, 1)),
                          Piece(Piece.WHITE, Piece.PAWN, (2, 2)),
                          Piece(Piece.WHITE, Piece.PAWN, (2, 3)),
                          Piece(Piece.WHITE, Piece.PAWN, (2, 4)),
                          Piece(Piece.WHITE, Piece.PAWN, (2, 5)),
                          Piece(Piece.WHITE, Piece.PAWN),
                          Piece(Piece.WHITE, Piece.PAWN),
                          Piece(Piece.WHITE, Piece.PAWN),
                          Piece(Piece.WHITE, Piece.ROOK, (1, 1)),
                          Piece(Piece.WHITE, Piece.ROOK, (1, 8)),
                          Piece(Piece.WHITE, Piece.KNIGHT, (1, 2)),
                          Piece(Piece.WHITE, Piece.KNIGHT),
                          Piece(Piece.WHITE, Piece.BISHOP),
                          Piece(Piece.WHITE, Piece.BISHOP),
                          Piece(Piece.WHITE, Piece.QUEEN),
                          Piece(Piece.WHITE, Piece.KING),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.PAWN),
                          Piece(Piece.BLACK, Piece.ROOK),
                          Piece(Piece.BLACK, Piece.ROOK),
                          Piece(Piece.BLACK, Piece.KNIGHT),
                          Piece(Piece.BLACK, Piece.KNIGHT),
                          Piece(Piece.BLACK, Piece.BISHOP),
                          Piece(Piece.BLACK, Piece.BISHOP),
                          Piece(Piece.BLACK, Piece.QUEEN),
                          Piece(Piece.BLACK, Piece.KING),
        ]

    def get_piece(self, row, column):
        for piece in self.pieces:
            r, c = piece.position
            if row == r and column == c:
                return piece

class Piece:
    WHITE = 0
    BLACK = 1

    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5

    def __init__(self, colour, type, position=(0,0)):
        self.colour = colour
        self.type = type
        self.position = position
