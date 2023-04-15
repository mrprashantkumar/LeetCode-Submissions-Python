class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and maze[p][q] == '.' and (p, q) not in visited
        
        n, m = len(maze), len(maze[0])
        visited = set()
        visited.add(tuple(entrance))
        qu = deque()
        for i in range(n):
            if maze[i][0] == '.' and (i, 0) not in visited:
                qu.append((i, 0))
                visited.add((i, 0))
            
            if maze[i][m-1] == '.' and (i, m-1) not in visited:
                qu.append((i, m-1))
                visited.add((i, m-1))
        
        for j in range(m):
            if maze[0][j] == '.' and (0, j) not in visited:
                qu.append((0, j))
                visited.add((0, j))
            
            if maze[n-1][j] == '.' and (n-1, j) not in visited:
                qu.append((n-1, j))
                visited.add((n-1, j))
        visited.remove(tuple(entrance))
        ans = 0
        while qu:
            # print(qu)
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                    if isvalid(x+dx, y+dy):
                        if [x+dx,y+dy] == entrance:
                            return ans+1
                        visited.add((x+dx, y+dy))
                        qu.append((x+dx, y+dy))  
            
            ans += 1
        
        return -1