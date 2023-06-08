class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            ind = bisect.bisect_right(grid[i][::-1], -1)
            ans += ind
        return ans