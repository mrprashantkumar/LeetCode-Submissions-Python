class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def isvalid(a, b):
            return 0 <= a < n and 0 <= b < m and land[a][b] == 1 and (a, b) not in visited

        def bfs(p, q):
            ans = [p, q]
            qu = deque()
            qu.append((p, q))
            visited.add((p, q))
            last = [p, q]
            while qu:
                l = len(qu)
                for _ in range(l):
                    x, y = qu.popleft()
                    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        if isvalid(x+dx, y+dy):
                            qu.append((x+dx, y+dy))
                            visited.add((x+dx, y+dy))
                            last = [x+dx, y+dy]
            
            ans += last
            return ans
        
        n, m = len(land), len(land[0])
        visited = set()
        res = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and (i, j) not in visited:
                    res.append(bfs(i, j))
        return res