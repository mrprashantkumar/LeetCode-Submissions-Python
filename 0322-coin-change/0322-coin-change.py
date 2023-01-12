class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(amount):
            if amount<0:
                return 100005
            
            if amount==0:
                return 0
            
            if dp[amount] != -1:
                return dp[amount]
            
            ans = 100005
            for i in coins:
                ans = min(ans, solve(amount-i))
            
            dp[amount] = ans+1
            return dp[amount]
        
        dp = [-1 for i in range(amount+1)]
        ans = solve(amount)
        return ans if ans<100000 else -1