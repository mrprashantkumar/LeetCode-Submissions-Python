class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.r1 = [0]*n
        self.r2 = [0]*n
        self.d1 = 0
        self.rd1 = 0
        self.c1 = [0]*n
        self.c2 = [0]*n
        self.d2 = 0
        self.rd2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.r1[row] += 1
            self.c1[col] += 1
            if row == col:
                self.d1 += 1
            if row + col == self.n-1:
                self.rd1 += 1
            if self.r1[row] == self.n or self.c1[col] == self.n or self.d1 == self.n or self.rd1 == self.n:
                return 1
            
        elif player == 2:
            self.r2[row] += 1
            self.c2[col] += 1
            if row == col:
                self.d2 += 1
            if row + col == self.n-1:
                self.rd2 += 1
            if self.r2[row] == self.n or self.c2[col] == self.n or self.d2== self.n or self.rd2 == self.n:
                return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)