class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def helper(i, paint):
            if i == n:
                return 0
            
            if dp[i][paint+1] != -1:
                return dp[i][paint+1]
            
            ans = 1000000007
            for j in range(3):
                if j != paint:
                    ans = min(ans, costs[i][j] + helper(i+1, j))
            
            dp[i][paint+1] = ans
            return dp[i][paint+1]
        
        n = len(costs)
        dp = [[-1]*4 for _ in range(n)]
        return helper(0, -1)