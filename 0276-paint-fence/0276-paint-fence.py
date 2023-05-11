class Solution:
    def numWays(self, n: int, k: int) -> int:
        def helper(i):
            if i == 0:
                return 0
            if i == 1:
                return k
            if i == 2:
                return k*k
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = (k-1) * (helper(i-1) + helper(i-2))
            return dp[i]
        
        dp = [-1] * (n+1)
        return helper(n)