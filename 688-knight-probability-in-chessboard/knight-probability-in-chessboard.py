class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<n
        
        dp = [[[0] * n for a in range(n)] for b in range(k + 1)]
        dp[0][row][column] = 1

        for moves in range(1, k+1):
            for x in range(n):
                for y in range(n):
                    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]:
                        newx, newy = x+dx, y+dy
                        if isvalid(newx, newy):
                            dp[moves][x][y] += dp[moves-1][newx][newy]
                    
                    dp[moves][x][y] /= 8
        
        return sum(dp[k][i][j] for i in range(n) for j in range(n))