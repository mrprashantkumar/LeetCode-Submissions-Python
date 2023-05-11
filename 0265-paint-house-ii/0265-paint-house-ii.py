class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        def helper(i, last):
            if i == n:
                return 0
            
            if dp[i][last+1] != -1:
                return dp[i][last+1]
            
            ans = 1000000007
            for j in range(k):
                if last != j:
                    cost = costs[i][j] + helper(i+1, j)
                    ans = min(ans, cost)
            
            dp[i][last+1] = ans
            return dp[i][last+1]
        
        n, k = len(costs), len(costs[0])
        dp = [[-1]*(k+1) for _ in range(n)]
        return helper(0, -1)