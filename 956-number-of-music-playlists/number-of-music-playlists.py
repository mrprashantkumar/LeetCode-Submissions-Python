class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0]*(n+1) for _ in range(goal+1)]
        dp[0][0] = 1

        for i in range(1, goal+1):
            for j in range(1, min(i, n)+1):
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % 1000000007
                if j > k:
                    dp[i][j] += dp[i-1][j]*(j-k)
                    dp[i][j] %= 1000000007
        
        return dp[goal][n]