class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def isvalid(p, q, val):
            return 0<=p<n and 0<=q<m and grid[p][q] == val
        
        def dfs(x, y, val, parent, seen):
            if (x, y) in seen:
                return True
            
            seen.add((x, y))
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if not parent or parent != (x+dx, y+dy):
                    if isvalid(x+dx, y+dy, val):
                        if dfs(x+dx, y+dy, val, (x, y), seen):
                            return True
            return False
        
        n, m = len(grid), len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if (i,  j) not in visited:
                    seen = set()
                    if dfs(i, j, grid[i][j], None, seen):
                        # print(i, j)
                        return True
        return False