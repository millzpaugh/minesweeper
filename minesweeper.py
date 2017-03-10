import random


class Board():

    def __init__(self, width, height, number_of_mines):
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines
        self.board = []

    def generate_board(self):
        for r in range(0, self.height):
            row = [0]*self.width
            self.board.append(row)

    def generate_random_cell(self):
        row = random.randint(0, self.height-1)
        column = random.randint(0, self.width-1)
        return row, column

    def assign_mines(self):
        total_mines = 0

        while total_mines < self.number_of_mines:
            row, column = self.generate_random_cell()

            if self.board[row][column] == 0:
                self.board[row][column] = "X"
                total_mines += 1

    def generate_range_constraints(self, cell):
        row, column = cell

        if row >= self.height or column >= self.width:
            raise ValueError("Cell is out of range")

        row_min = max(0, row - 1)
        column_min = max(0, column-1)

        row_max = min(row+2, self.height)
        column_max = min(column+2, self.width)

        return (row_min, row_max), (column_min, column_max)

    def count_neighbor_mine_cells(self, origin_cell):
        if self.board[origin_cell[0]][origin_cell[1]] != "X":
            row_range, column_range = self.generate_range_constraints(
                origin_cell)
            mine_count = 0
            for r in range(row_range[0], row_range[1]):
                for i in range(column_range[0], column_range[1]):
                    if self.board[r][i] == "X":
                        mine_count += 1

            self.board[origin_cell[0]][origin_cell[1]] = mine_count

    def count_all_mines(self):
        for r in range(0, self.height):
            for i in range(0, self.width):
                cell = (r, i)
                self.count_neighbor_mine_cells(cell)
