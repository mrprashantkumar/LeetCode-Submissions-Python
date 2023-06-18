class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m

        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]

            res = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if isvalid(x+dx, y+dy) and grid[x][y] < grid[x+dx][y+dy]:
                    res += dfs(x+dx, y+dy)
            
            dp[x][y] = res
            return res

        n, m = len(grid), len(grid[0])
        dp = [[0]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += dfs(i, j)
                ans %= 1000000007
        return ans