class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        row, col = [0]*n, [0]*m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        ans = [ [0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                ans[i][j] = row[i] + col[j] - (n-row[i]) - (m-col[j])
        
        return ans