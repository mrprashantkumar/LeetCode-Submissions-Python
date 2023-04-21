class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        def helper(i, prof, members):
            if i >= l:
                return int(prof >= minProfit)
            
            if dp[i][prof][members] != -1:
                return dp[i][prof][members]
            
            notTake = helper(i+1, prof, members)
            take = 0
            if members+group[i] <= n:
                take = helper(i+1, min(minProfit, prof+profit[i]), members+group[i])
            
            dp[i][prof][members] = (take+notTake)%1000000007
            return dp[i][prof][members]
            
                
        l = len(profit)
        dp = [[[-1]*(n+1) for i in range(minProfit+1)] for j in range(l)]
        return helper(0, 0, 0)%1000000007