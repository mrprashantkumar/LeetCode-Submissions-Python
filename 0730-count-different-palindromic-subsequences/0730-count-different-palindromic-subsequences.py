class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        def helper(i, j):
            if i>j:
                return 0
            if i == j:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                left, right = i + 1, j - 1
                
                while left <= right and s[left] != s[i]:
                    left += 1
                while left <= right and s[right] != s[i]:
                    right -= 1
                    
                if left > right:
                    dp[i][j] = helper(i+1, j-1)*2 + 2
                elif left == right:
                    dp[i][j] = helper(i+1, j-1)*2 + 1
                else:
                    dp[i][j] = helper(i+1, j-1)*2 - helper(left+1, right-1)
            else:
                dp[i][j] = helper(i+1, j) + helper(i, j-1) - helper(i+1, j-1)
            
            dp[i][j] %= 1000000007
            
            return dp[i][j]
        
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        return helper(0, n-1)