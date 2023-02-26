class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def helper(i, j):
            if i==n:
                return sum(ord(s2[k]) for k in range(j, m))
            if j==m:
                return sum(ord(s1[k]) for k in range(i, n))
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j]:
                dp[i][j] = helper(i+1, j+1)
                return dp[i][j]
            else:
                rems1 = ord(s1[i])+helper(i+1, j)
                rems2 = ord(s2[j])+helper(i, j+1)
                dp[i][j] = min(rems1, rems2)
                return dp[i][j]
        
        n, m = len(s1), len(s2)
        dp = [[-1]*m for _ in range(n)]
        return helper(0, 0)