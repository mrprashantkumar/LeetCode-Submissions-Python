class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if m == 1:
            return n
        
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        colCount = [row[:] for row in grid]
        for i in range(1, n):
            for j in range(m):
                colCount[i][j] += colCount[i-1][j]
        # print(colCount)
        
        ans = 0
        for j in range(m):
            oneCount = max(colCount[n-1][j], n - colCount[n-1][j])
            ans += oneCount * (2**(m - j - 1))
        return ans
