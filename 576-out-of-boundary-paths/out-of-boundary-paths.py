class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def isvalid(p, q):
            return 0 <= p < m and 0 <= q < n
        
        @cache
        def helper(x, y, movesLeft):
            if not isvalid(x, y):
                return 1

            if movesLeft == 0:
                return 0
            
            ans = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ans += helper(x+dx, y+dy, movesLeft-1)
            return ans % 1000000007
        
        return helper(startRow, startColumn, maxMove)