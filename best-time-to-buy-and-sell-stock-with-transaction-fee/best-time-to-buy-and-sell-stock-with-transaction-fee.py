class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def helper(i, alreadyBuyed):
            if i == n:
                return 0
            
            if dp[i][alreadyBuyed] != -1:
                return dp[i][alreadyBuyed]

            if alreadyBuyed:
                sell = (prices[i] - fee) + helper(i+1, 0)
                notSell = helper(i+1, 1)
                profit = max(sell, notSell)
            else:
                buy = -prices[i] + helper(i+1, 1)
                notBuy = helper(i+1, 0)
                profit = max(buy, notBuy)
            
            dp[i][alreadyBuyed] = profit
            return profit
        
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        return helper(0, 0)