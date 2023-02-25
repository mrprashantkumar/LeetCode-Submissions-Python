class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = 1000000007
        for i in prices:
            if i<buy:
                buy = i
            else:
                ans = max(ans, i-buy)
        return ans