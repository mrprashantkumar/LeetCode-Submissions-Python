class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        yd, od = Counter(), Counter()
        for i in range(n//2):
            for j in range(n):
                if i == j or i+j == n-1:
                    yd[grid[i][j]] += 1
                else:
                    od[grid[i][j]] += 1
        
        for i in range(n//2, n):
            for j in range(n):
                if j == n//2:
                    yd[grid[i][j]] += 1
                else:
                    od[grid[i][j]] += 1
        yc = n + n//2
        oc = n*n - yc
        ans = n*n
        for i in range(3):
            for j in range(3):
                if i != j:
                    ans = min(ans, yc - yd[i] + oc - od[j])
        return ans
