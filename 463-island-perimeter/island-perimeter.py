class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def isvalid(p, q):
            return 0 <= p < n and 0 <= q < m and grid[p][q] == 1 and (p, q) not in visited

        def helper(x, y):
            visited.add((x, y))

            ans = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if isvalid(x+dx, y+dy):
                    ans += helper(x+dx, y+dy)
                else:
                    if (x+dx, y+dy) not in visited:
                        ans += 1
            return ans
        
        n, m = len(grid), len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    print(i, j)
                    return helper(i, j)