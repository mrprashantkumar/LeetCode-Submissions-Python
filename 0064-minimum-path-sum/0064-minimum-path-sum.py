class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = grid
        
        for i in range(1, n):
            dp[i][0] += dp[i-1][0]
        for j in range(1, m):
            dp[0][j] += dp[0][j-1]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[n-1][m-1]