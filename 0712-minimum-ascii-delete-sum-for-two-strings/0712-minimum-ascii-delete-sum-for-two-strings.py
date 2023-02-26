class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][m] = sum(ord(s1[k]) for k in range(i, n))
        for j in range(m):
            dp[n][j] = sum(ord(s2[k]) for k in range(j, m))
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    rems1 = ord(s1[i])+dp[i+1][j]
                    rems2 = ord(s2[j])+dp[i][j+1]
                    dp[i][j] = min(rems1, rems2)
        return dp[0][0]
        
        
        
#         def helper(i, j):
#             if i==n:
#                 return sum(ord(s2[k]) for k in range(j, m))
#             if j==m:
#                 return sum(ord(s1[k]) for k in range(i, n))
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             if s1[i] == s2[j]:
#                 dp[i][j] = helper(i+1, j+1)
#                 return dp[i][j]
#             else:
#                 rems1 = ord(s1[i])+helper(i+1, j)
#                 rems2 = ord(s2[j])+helper(i, j+1)
#                 dp[i][j] = min(rems1, rems2)
#                 return dp[i][j]
        
        # n, m = len(s1), len(s2)
        # dp = [[-1]*m for _ in range(n)]
#         return helper(0, 0)