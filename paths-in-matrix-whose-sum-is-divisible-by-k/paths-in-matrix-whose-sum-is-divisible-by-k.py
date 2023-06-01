class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        def helper(x, y, sumsofar):
            sumsofar %= k
            if x >= n or y >= m:
                return 0
            if x == n-1 and y == m-1:
                sumsofar += grid[x][y]
                return int(sumsofar % k == 0)

            if dp[x][y][sumsofar] != -1:
                return dp[x][y][sumsofar]
            
            right = helper(x, y+1, (sumsofar + grid[x][y]%k))
            down = helper(x+1, y, (sumsofar + grid[x][y]%k))

            dp[x][y][sumsofar] = (right+down)%1000000007
            return dp[x][y][sumsofar]
        
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                grid[i][j] %= k
        dp = [[[-1]*(k) for a in range(m+1)] for b in range(n+1)]
        return helper(0, 0, 0)