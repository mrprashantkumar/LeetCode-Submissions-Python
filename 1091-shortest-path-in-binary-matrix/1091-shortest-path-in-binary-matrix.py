class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and (p, q) not in visited and grid[p][q] == 0
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n, m = len(grid), len(grid[0])
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0),(1,1)]
        ans = 1
        qu = deque([(0, 0)])
        visited = set()
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                if x == n-1 and y == m-1:
                    return ans
                for dx, dy in dirs:
                    if isvalid(x+dx, y+dy):
                        visited.add((x+dx, y+dy))
                        qu.append((x+dx, y+dy))
                
            ans += 1
        
        return -1