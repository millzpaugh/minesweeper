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
            flag = self.board[row][column]

            if flag == 0:
                self.board[row][column] = "X"
                total_mines += 1
            else:
                continue

    def generate_range_constraints(self, cell):
        row, column = cell

        if row >= self.height or column >= self.width:
            raise ValueError("Cell is out of range")

        if row == 0:
            row_min = row
        else:
            row_min = row - 1

        if column == 0:
            column_min = column
        else:
            column_min = column - 1

        if row == self.height-1:
            row_max = row + 1
        else:
            row_max = row + 2

        if column == self.width-1:
            column_max = column + 1
        else:
            column_max = column + 2

        column_range = (column_min, column_max)
        row_range = (row_min, row_max)
        return row_range, column_range

    def count_neighbor_mine_cells(self, origin_cell):
        if self.board[origin_cell[0]][origin_cell[1]] != "X":
            row_range, column_range = self.generate_range_constraints(
                origin_cell)
            cells = []
            for r in range(row_range[0], row_range[1]):
                for i in range(column_range[0], column_range[1]):
                    cell = self.board[r][i]
                    if cell != origin_cell:
                        cells.append(cell)
            mine_count = cells.count("X")

            self.board[origin_cell[0]][origin_cell[1]] = mine_count

    def count_all_mines(self):
        for r in range(0, self.height):
            for i in range(0, self.width):
                cell = (r, i)
                self.count_neighbor_mine_cells(cell)
