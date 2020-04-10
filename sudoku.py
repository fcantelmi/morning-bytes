import os
import re


class BacktrackingSolver:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def possible(self, row, col, value):
        if value in self.puzzle.row_values(row):
            return False

        if value in self.puzzle.col_values(col):
            return False

        if value in self.puzzle.box_values(row, col):
            return False

        return True

    def solve(self, start_row=0, start_col=0):
        for row in range(9):
            for col in range(9):
                if self.puzzle.get_value(row, col) is None:
                    for value in range(1, 10):
                        if self.possible(row, col, value):
                            self.puzzle.set_value(row, col, value)
                            if self.solve(start_row=row, start_col=col) is False:
                                self.puzzle.set_value(row, col, None)
                    return False

        print(self.puzzle)
        return True


class Puzzle:

    @classmethod
    def parse(cls, p):
        no_whitespace = re.sub(r"\s+", "", p)
        values = [int(val) if val in '123456789' else None for val in no_whitespace]

        return cls(values)

    def __init__(self, values):
        self.values = values

    def __str__(self):
        p = ""

        for row in range(9):
            row_index = 9 * row
            split = ["." if it is None else str(it) for it in self.values[row_index:row_index + 9]]
            p += " ".join(split)
            p += os.linesep

        return p

    def set_value(self, row, col, value):
        self.values[row * 9 + col] = value

    def get_value(self, row, col):
        return self.values[row * 9 + col]

    def box_values(self, row, col):
        box_row = (row // 3) * 3  # returns 0, 3, or 6
        box_col = (col // 3) * 3  # returns 0, 3, or 6

        values = [self.get_value(box_row + it_row, box_col + it_col) for it_row in range(3) for it_col in range(3)]
        return frozenset(values)

    def row_values(self, row):
        index = 9 * row
        values = self.values[index:index + 9]
        return frozenset(values)

    def col_values(self, col):
        values = self.values[col::9]
        return frozenset(values)


def main():
    unsolved = """
        .  .  .  .  .  .  .  1  5
        .  4  9  .  .  .  .  .  .
        2  .  .  3  .  1  7  .  .
        8  .  .  2  .  .  .  9  .
        .  9  .  .  .  .  .  7  .
        .  7  .  .  .  6  .  .  1
        .  .  4  9  .  5  .  .  7
        .  .  .  .  .  .  5  4  .
        6  1  .  .  .  .  .  .  .
    """

    puzzle = Puzzle.parse(unsolved)
    print(puzzle)
    solver = BacktrackingSolver(puzzle)
    solver.solve()


if __name__ == '__main__':
    main()
