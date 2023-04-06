class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 0 and (p, q) not in visited
        
        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if check(x+dx, y+dy):
                    dfs(x+dx, y+dy)
            
        n, m = len(grid), len(grid[0])
        
        qu = deque()
        for i in range(n):
            if grid[i][0] == 0:
                qu.append((i, 0))
            if grid[i][m-1] == 0:
                qu.append((i, m-1))
        
        for j in range(m):
            if grid[0][j] == 0:
                qu.append((0, j))
            if grid[n-1][j] == 0:
                qu.append((n-1, j))
        
        visited = set()
        while qu:
            x, y = qu.popleft()
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if check(x+dx, y+dy):
                    qu.append((x+dx, y+dy))
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if check(i, j):
                    dfs(i, j)
                    ans += 1
        return ans
        