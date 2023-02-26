class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(i, j):
            if i==n:
                return m-j
            if j==m:
                return n-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = helper(i+1, j+1)
                return dp[i][j]
            else:
                rep = helper(i+1, j+1)
                dele = helper(i+1, j)
                ins = helper(i, j+1)
                dp[i][j] = 1 + min(rep, dele, ins)
                return dp[i][j]
        
        n, m = len(word1), len(word2)
        dp = [[-1]*(m) for _ in range(n)]
        return helper(0, 0)