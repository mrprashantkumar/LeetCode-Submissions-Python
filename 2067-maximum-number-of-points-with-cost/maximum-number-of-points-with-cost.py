class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = points[0]

        for i in range(1, n):
            pref = [0]*m
            suff = [0]*m
            curr = [0]*m

            pref[0] = dp[0]
            for j in range(1, m):
                pref[j] = max(pref[j-1] - 1, dp[j])
            
            suff[-1] = dp[-1]
            for j in range(m-2, -1, -1):
                suff[j] = max(suff[j+1] - 1, dp[j])
            
            for j in range(m):
                curr[j] = points[i][j] + max(pref[j], suff[j])
            
            dp = curr
        return max(dp)