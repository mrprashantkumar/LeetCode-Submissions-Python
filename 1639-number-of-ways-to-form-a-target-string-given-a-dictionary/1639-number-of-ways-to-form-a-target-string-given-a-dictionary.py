class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        def f(i, j):
            if j == 0:
                return 1 if i == 0 else 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = f(i, j - 1)
            
            if i > 0:
                dp[i][j] += (cnt[ord(target[i - 1]) - ord('a')][j - 1] * f(i - 1, j - 1))
                
            dp[i][j] %= 1000000007
            return dp[i][j]
        
        m = len(target)
        k = len(words[0])
        cnt = [[0] * k for _ in range(26)]
        
        for j in range(k):
            for word in words:
                cnt[ord(word[j]) - ord('a')][j] += 1
                
        dp = [[-1] * (k + 1) for _ in range(m + 1)]
        return f(m, k)