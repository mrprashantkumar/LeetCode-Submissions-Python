class Solution:
    def minInsertions(self, s: str) -> int:
        def helper(i, j):
            if i >= j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] != s[j]:
                ans = 1 + min(helper(i+1, j), helper(i, j-1))
            else:
                ans = helper(i+1, j-1)
            
            dp[i][j] = ans
            return dp[i][j]
        
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        return helper(0, n-1)