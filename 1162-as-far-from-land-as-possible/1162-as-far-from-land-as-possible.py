class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        qu = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    qu.append((i,j))
        
        l = len(qu)
        if l==0 or l==n*m:
            return -1
        
        ans = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        visited = set()
        while qu:
            for i in range(len(qu)):
                node = qu.popleft()
                x, y = node
                visited.add(node)

                for dx, dy in dirs:
                    newX, newY = x+dx, y+dy
                    if 0 <= newX < n and 0 <= newY < m:
                            if (newX, newY) not in visited:
                                if grid[newX][newY] == 0: 
                                    qu.append((newX, newY))
                                    grid[newX][newY] = 1
            ans += 1
        return ans-1