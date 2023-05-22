class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and rooms[p][q] == 2147483647

        n, m = len(rooms), len(rooms[0])
        qu = deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    qu.append((i, j))
        dist = 1
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if isvalid(x+dx, y+dy):
                        rooms[x+dx][y+dy] = dist
                        qu.append((x+dx, y+dy))
            dist += 1