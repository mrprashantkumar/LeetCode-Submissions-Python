class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        ans = 0
        for i in range(n-1):
            ans = max(ans, points[i+1][0] - points[i][0])
        return ans