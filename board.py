import random

class Board:
    def __init__(self):
        self.size = 5
        self.symbols = ['A', 'B', 'C', 'D']
        self.grid = self.create_board()

    def create_board(self):
        board = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(random.choice(self.symbols))
            board.append(row)
        return board

    def display(self):
        print("\nGame Board:")
        for row in self.grid:
            print(" ".join(row))

    def is_valid_move(self, move):
        r1, c1, r2, c2 = move

        if abs(r1 - r2) + abs(c1 - c2) != 1:
            return False

        if self.grid[r1][c1] != self.grid[r2][c2]:
            return False

        return True

    def apply_move(self, move):
        if not self.is_valid_move(move):
            return False

        r1, c1, r2, c2 = move
        self.grid[r2][c2] = self.grid[r1][c1]
        self.grid[r1][c1] = random.choice(self.symbols)
        return True
