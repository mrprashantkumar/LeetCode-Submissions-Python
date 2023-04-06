class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1 and (p, q) not in visited
        
        def dfs(x, y):
            area = 1
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if check(x+dx, y+dy):
                    area += dfs(x+dx, y+dy)
            return area
        
        n, m = len(grid), len(grid[0])
        visited = set()
        ans = 0
        for i in range(n):
            for j in range(m):
                if check(i, j):
                    ans = max(ans, dfs(i, j))
        return ans