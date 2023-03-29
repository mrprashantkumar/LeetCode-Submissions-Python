class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        def helper(i, time):
            if i==n:
                return 0
            
            if dp[i][time] != -1:
                return dp[i][time]
            
            notTake = helper(i+1, time)
            take = satisfaction[i]*time + helper(i+1, time+1)
            
            dp[i][time] = max(take, notTake)
            return max(take, notTake)
        
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return helper(0, 1)