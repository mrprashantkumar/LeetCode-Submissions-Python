class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 0 and (p, q) not in visited
        
        n, m = len(grid), len(grid[0])
        qu = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    qu.append((i,j))
        
        l = len(qu)
        if l==0 or l==n*m:
            return -1
        
        ans = -1
        visited = set()
        while qu:
            l = len(qu)
            for i in range(l):
                x, y = qu.popleft()
                visited.add((x, y))
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if check(x+dx, y+dy):
                        qu.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            ans += 1
        return ans