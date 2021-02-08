import unittest

from board import Board, Piece


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_created(self):
        self.assertIsNotNone(self.board)

    def test_pieces_count(self):
        self.assertEqual(len(self.board.pieces), 32)

    def test_pieces_colour(self):
        self.assertEqual(len([p for p in self.board.pieces if p.colour == Piece.WHITE]), 16)
        self.assertEqual(len([p for p in self.board.pieces if p.colour == Piece.BLACK]), 16)

    def test_piece_type(self):
        for colour in [Piece.BLACK, Piece.WHITE]:
            pieces = [p for p in self.board.pieces if p.colour == colour]
            self.assertEqual(len([p for p in pieces if p.type == Piece.PAWN]), 8)
            self.assertEqual(len([p for p in pieces if p.type == Piece.ROOK]), 2)
            self.assertEqual(len([p for p in pieces if p.type == Piece.KING]), 1)

    def test_piece_position(self):
        self.assertEqual(self.board.get_piece(2, 1).colour, Piece.WHITE)


if __name__ == '__main__':
    unittest.main()
