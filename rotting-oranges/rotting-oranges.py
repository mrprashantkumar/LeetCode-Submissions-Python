class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 1
        n, m = len(grid), len(grid[0])
        qu = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    qu.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if not qu and fresh == 0:
            return 0
            
        ans = 0
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if isvalid(x+dx, y+dy):
                        grid[x+dx][y+dy] = 2
                        fresh -= 1
                        qu.append((x+dx, y+dy))
                        
            ans += 1
        return ans-1 if fresh==0 else -1