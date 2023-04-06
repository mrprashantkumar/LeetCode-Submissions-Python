class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(p, q):
            return 0<=p<n and 0<=q<m and grid[p][q] == 'O' and (p, q) not in visited
        
        n, m = len(grid), len(grid[0])
        qu = deque()
        for i in range(n):
            if grid[i][0] == 'O':
                qu.append((i, 0))
            if grid[i][m-1] == 'O':
                qu.append((i, m-1))
        
        for j in range(m):
            if grid[0][j] == 'O':
                qu.append((0, j))
            if grid[n-1][j] == 'O':
                qu.append((n-1, j))
        # print(qu)
        visited = set()
        while qu:
            x, y = qu.popleft()
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if check(x+dx, y+dy):
                    qu.append((x+dx, y+dy))
        
        for i in range(n):
            for j in range(m):
                if check(i, j):
                    grid[i][j] = 'X'
