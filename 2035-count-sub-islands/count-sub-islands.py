class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0 <= p < n and 0 <= q < m and grid2[p][q] == 1 and (p, q) not in visited

        def get_islands_from_grid2(x, y):
            visited.add((x, y))
            res = [(x, y)]
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if isvalid(x+dx, y+dy):
                    res += get_islands_from_grid2(x+dx, y+dy)
            
            return res
        
        n, m = len(grid1), len(grid1[0])
        islands = []
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    islands.append(get_islands_from_grid2(i, j))
        
        ans = 0
        for island in islands:
            f = True
            for x, y in island:
                if grid1[x][y] == 0:
                    f = False
                    break
            
            if f:
                ans += 1
        return ans