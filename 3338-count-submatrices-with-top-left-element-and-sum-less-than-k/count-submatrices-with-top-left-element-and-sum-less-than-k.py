class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0
        n, m = len(grid), len(grid[0])
        pref = [[0]*(m+1) for _ in range(n+1)]

        ans = 0
        for i in range(n):
            for j in range(m):
                pref[i+1][j+1] = grid[i][j] + pref[i+1][j] + pref[i][j+1] - pref[i][j]
                if pref[i+1][j+1] <= k:
                    ans += 1
        return ans