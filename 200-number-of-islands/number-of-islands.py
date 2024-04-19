class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == '1' and (p, q) not in visited
        
        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if check(x+dx, y+dy):
                    dfs(x+dx, y+dy)
        
        n, m = len(grid), len(grid[0])
        visited = set()
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        return ans