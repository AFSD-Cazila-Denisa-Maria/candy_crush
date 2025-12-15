class Engine:
    def __init__(self, board):
        self.board = board
        self.score = 0
        self.level = 1

    def detect_formations(self):
        g = self.board.grid
        R, C = self.board.rows, self.board.cols
        found = []

        # linii orizontale
        for r in range(R):
            c = 0
            while c < C:
                v = g[r][c]
                if v == 0:
                    c += 1
                    continue
                start = c
                while c < C and g[r][c] == v:
                    c += 1
                length = c - start
                if length >= 3:
                    score = 5 if length == 3 else 10 if length == 4 else 50
                    found.append((score, [(r, x) for x in range(start, c)]))

        # linii verticale
        for c in range(C):
            r = 0
            while r < R:
                v = g[r][c]
                if v == 0:
                    r += 1
                    continue
                start = r
                while r < R and g[r][c] == v:
                    r += 1
                length = r - start
                if length >= 3:
                    score = 5 if length == 3 else 10 if length == 4 else 50
                    found.append((score, [(x, c) for x in range(start, r)]))

        # L și T
        for r in range(R - 2):
            for c in range(C - 2):
                v = g[r][c]
                if v == 0:
                    continue

                # L
                if g[r+1][c] == v and g[r+2][c] == v and g[r][c+1] == v and g[r][c+2] == v:
                    found.append((20, [(r,c),(r+1,c),(r+2,c),(r,c+1),(r,c+2)]))

                # T
                if g[r][c+1] == v and g[r][c+2] == v and g[r+1][c+1] == v and g[r+2][c+1] == v:
                    found.append((30, [(r,c+1),(r+1,c+1),(r+2,c+1),(r,c),(r,c+2)]))

        return found

    def cascade_step(self):
        formations = self.detect_formations()
        if not formations:
            return False

        used = set()
        for score, cells in sorted(formations, key=lambda x: -x[0]):
            if any(cell in used for cell in cells):
                continue
            for r, c in cells:
                self.board.grid[r][c] = 0
                used.add((r, c))
            self.score += score

        self.level = self.score // 50 + 1
        self.board.apply_gravity()
        self.board.refill()
        return True

    def try_swap(self, a, b):
        r1, c1 = a
        r2, c2 = b
        self.board.grid[r1][c1], self.board.grid[r2][c2] = \
            self.board.grid[r2][c2], self.board.grid[r1][c1]

        if self.detect_formations():
            return True

        self.board.grid[r1][c1], self.board.grid[r2][c2] = \
            self.board.grid[r2][c2], self.board.grid[r1][c1]
        return False
