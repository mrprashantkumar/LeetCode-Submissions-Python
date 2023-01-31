class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        def helper(i, prev):
            if i==n:
                return 0
            
            if dp[i][prev] != -1:
                return dp[i][prev]
            
            
            notTake = helper(i+1, prev)
            take = 0
            if prev == -1 or nums[i][1]>=nums[prev][1]:
                take = nums[i][1] + helper(i+1, i)
            
            dp[i][prev] = max(take, notTake)
            return dp[i][prev]
            
        n = len(ages)
        nums = sorted([(i, j) for i, j in zip(ages, scores)])
        dp = [[-1]*(n) for _ in range(n)]
        return helper(0, -1)