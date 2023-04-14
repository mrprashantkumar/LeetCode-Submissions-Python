class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    ans1 = dp[i+1][j]
                    ans2 = dp[i][j-1]
                    dp[i][j] = max(ans1, ans2)
        
        return dp[0][n-1]
        
        
#         def helper(i, j, s):
#             if i>j:
#                 return 0
#             if i==j:
#                 return 1
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             if s[i]==s[j]:
#                 dp[i][j] = 2+helper(i+1, j-1, s)
#                 return dp[i][j]
#             else:
#                 ans1 = helper(i+1, j, s)
#                 ans2 = helper(i, j-1, s)
#                 dp[i][j] = max(ans1, ans2)
#                 return dp[i][j]
        
#         return helper(0, n-1, s)