class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def helper(x, y1, y2):
            if x == n-1:
                return 0
            
            ans = 0
            for dy1 in range(-1, 2):
                for dy2 in range(-1, 2):
                    if 0 <= y1+dy1 < m and 0 <= y2+dy2 < m:
                        if y1+dy1 == y2+dy2:
                            ans = max(ans, grid[x+1][y1+dy1] + helper(x+1, y1+dy1, y2+dy2))
                        else:
                            ans = max(ans, grid[x+1][y1+dy1] + grid[x+1][y2+dy2] + helper(x+1, y1+dy1, y2+dy2))
            return ans

        n, m = len(grid), len(grid[0])
        return grid[0][0] + grid[0][m-1] + helper(0, 0, m-1)