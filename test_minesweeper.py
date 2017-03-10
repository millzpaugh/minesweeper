from minesweeper import *

import unittest


class TestMine(unittest.TestCase):

    def setUp(self):
        self.board = Board(width=4, height=3, number_of_mines=4)

    def test_generate_board(self):
        self.board.generate_board()

        b = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.board.board, b)

        self.board.assign_mines()

        mine_count = 0
        for r in self.board.board:
            c = r.count("X")
            mine_count += c

        self.assertEqual(mine_count, self.board.number_of_mines)

    def test_generate_range_constraints(self):
        row_range, column_range = self.board.generate_range_constraints((1, 2))

        self.assertEqual(row_range, (0, 3))
        self.assertEqual(column_range, (1, 4))

        with self.assertRaises(ValueError):
            self.board.generate_range_constraints((7, 10))

    def test_count_neighbor_cells(self):
        self.board.board = [['X', 0, 'X', 0],
                            ['X', 0, 0, 'X'],
                            [0, 'X', 'X', 0]]
        self.board.count_neighbor_mine_cells((1, 1))

        self.assertEqual(self.board.board[1][1], 5)
