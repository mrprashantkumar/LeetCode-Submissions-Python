class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0 <= p < n and 0 <= q < m and (p, q) not in visited and grid[p][q] > 0

        def dfs(x, y):
            visited.add((x, y))
            ans = grid[x][y]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if isvalid(x+dx, y+dy):
                    ans = max(ans, grid[x][y] + dfs(x+dx, y+dy))

            visited.remove((x, y))
            return ans
        
        n, m = len(grid), len(grid[0])
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    visited = set()
                    res = max(res, dfs(i, j))
        
        return res