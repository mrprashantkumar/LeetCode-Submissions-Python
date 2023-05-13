class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def helper(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            
            if dp[i] != -1:
                return dp[i]
            
            ans = 0
            ans += helper(i-zero)
            ans += helper(i-one)
            ans %= 1000000007
            
            dp[i] = ans
            return dp[i]
            
        
        dp = [-1]*(high+1)
        ans=0
        for i in range(low, high+1):
            ans += helper(i)
            ans %= 1000000007
        return ans%1000000007