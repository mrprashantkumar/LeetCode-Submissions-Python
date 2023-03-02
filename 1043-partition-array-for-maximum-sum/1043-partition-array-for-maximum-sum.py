class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
#         def helper(i):
#             if i==n:
#                 return 0
            
#             if dp[i] != -1:
#                 return dp[i]
#             ans = 0
#             maxsofar = arr[i]
#             for j in range(i, min(n, i+k)):
#                 maxsofar = max(maxsofar, arr[j])
#                 smans = (j-i+1)*maxsofar + helper(j+1)
#                 ans = max(ans, smans)
            
#             dp[i] = ans
#             return ans
        
#         n = len(arr)
#         dp = [-1]*n
#         return helper(0)
        
        n = len(arr)
        dp = [-1]*(n+1)
        
        for i in range(n-1, -1, -1):
            ans = 0
            maxsofar = arr[i]
            for j in range(i, min(n, i+k)):
                maxsofar = max(maxsofar, arr[j])
                smans = (j-i+1)*maxsofar + dp[j+1]
                ans = max(ans, smans)
            
            dp[i] = ans
        
        return dp[0]+1