class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def countIslands():
            def isvalid(p, q):
                return 0<=p<n and 0<=q<m and grid[p][q] == 1 and (p, q) not in visited
            
            def dfs(x, y):
                visited.add((x, y))
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if isvalid(x+dx, y+dy):
                        dfs(x+dx, y+dy)
                    
            ans = 0
            visited = set()
            for i in range(n):
                for j in range(m):
                    if isvalid(i, j):
                        dfs(i, j)
                        ans += 1
            return ans
        
        
        n, m = len(grid), len(grid[0])
        count = countIslands()
        if count > 1 or count == 0:
            return 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    c = countIslands()
                    if c > 1 or c == 0:
                        return 1
                    grid[i][j] = 1
        
        return 2