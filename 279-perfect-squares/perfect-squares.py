class Solution:
    def numSquares(self, n: int) -> int:
        def helper(n):
            if n<=0:
                return 0
            if n==1:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            ans = 100005
            r = int(sqrt(n))
            for i in range(r, 0, -1):
                ans = min(ans, 1+helper(n-(i*i)))
            
            dp[n] = ans
            return ans
        
        dp = [-1]*(n+1)
        return helper(n)