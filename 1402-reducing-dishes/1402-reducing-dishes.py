class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         def helper(i, time):
#             if i==n:
#                 return 0
            
#             if dp[i][time] != -1:
#                 return dp[i][time]
            
#             notTake = helper(i+1, time)
#             take = satisfaction[i]*time + helper(i+1, time+1)
            
#             dp[i][time] = max(take, notTake)
#             return max(take, notTake)
        
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[0]*(n+2) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for time in range(n, 0, -1):
                notTake = dp[i+1][time]
                take = satisfaction[i]*time + dp[i+1][time+1]
                dp[i][time] = max(take, notTake)
        
        return dp[0][1]