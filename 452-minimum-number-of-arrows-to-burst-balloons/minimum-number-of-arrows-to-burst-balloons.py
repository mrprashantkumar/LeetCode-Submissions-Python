class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        ans = 1
        common = points[0]
        for i in range(1, n):
            if points[i][0] <= common[1]:
                common[1] = min(common[1], points[i][1])
            else:
                ans += 1
                common = points[i]
        
        return ans