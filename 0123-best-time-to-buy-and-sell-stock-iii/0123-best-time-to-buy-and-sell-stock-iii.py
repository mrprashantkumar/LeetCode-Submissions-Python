class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, canbuy, k):
            if k==0 or i==n:
                return 0
            
            if dp[i][canbuy][k] != -1:
                return dp[i][canbuy][k]
            
            if canbuy:
                buy = -prices[i]+helper(i+1, 0, k)
                notbuy = helper(i+1, 1, k)
                profit = max(buy, notbuy)
            else:
                sell = prices[i]+helper(i+1, 1, k-1)
                notsell = helper(i+1, 0, k)
                profit = max(sell, notsell)
            
            dp[i][canbuy][k] = profit
            return profit
        
        n = len(prices)
        dp = [[[-1]*3 for i in range(2)] for j in range(n)] 
        return helper(0, 1, 2)