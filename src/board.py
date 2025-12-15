import random

COLORS = [1, 2, 3, 4]

class Board:
    def __init__(self, rows=11, cols=11):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice(COLORS) for _ in range(cols)] for _ in range(rows)]

    def apply_gravity(self):
        for c in range(self.cols):
            col = [self.grid[r][c] for r in range(self.rows) if self.grid[r][c] != 0]
            zeros = [0] * (self.rows - len(col))
            new_col = zeros + col
            for r in range(self.rows):
                self.grid[r][c] = new_col[r]

    def refill(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 0:
                    self.grid[r][c] = random.choice(COLORS)
