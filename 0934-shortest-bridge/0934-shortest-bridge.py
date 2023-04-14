class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<n and (p, q) not in visited
        
        def dfs(x, y):
            visited.add((x, y))
            qu.append((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if isvalid(x+dx, y+dy) and grid[x+dx][y+dy] == 1:
                    dfs(x+dx, y+dy)
                    
        n = len(grid)
        qu = deque()
        visited = set()
        for i in range(n):
            f = False
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    f = True
                    break
            if f:
                break
                
        ans = 0
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if isvalid(x+dx, y+dy):
                        p, q = x+dx, y+dy
                        if grid[p][q] == 0:
                            visited.add((p, q))
                            qu.append((p, q))
                        else:
                            return ans
            ans += 1
        