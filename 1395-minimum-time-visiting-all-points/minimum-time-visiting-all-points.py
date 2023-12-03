class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(n-1):
            a, b = points[i+1]
            c, d = points[i]
            ans += max(abs(a-c), abs(b-d))
        return ans