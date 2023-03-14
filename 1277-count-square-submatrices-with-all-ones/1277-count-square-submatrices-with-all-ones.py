class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = matrix
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        
        ans = 0
        for row in dp:
            for i in row:
                ans += i
        return ans