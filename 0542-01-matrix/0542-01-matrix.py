class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and mat[p][q] == 1 and (p, q) not in visited
        
        n, m = len(mat), len(mat[0])
        ans = [[0]*m for _ in range(n)]
        
        visited = set()
        qu = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    qu.append((i, j))
        
        steps = 1
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(-1,0), (0,-1), (0,1), (1,0)]:
                    if isvalid(x+dx, y+dy):
                        visited.add((x+dx, y+dy))
                        qu.append((x+dx, y+dy))
                        ans[x+dx][y+dy] = steps
            steps += 1
        return ans