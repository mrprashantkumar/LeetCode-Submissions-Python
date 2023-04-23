class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        def helper(i):
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            ans = 0
            currNum = 0
            for j in range(i, n):
                currNum *= 10
                currNum += ord(s[j]) - ord('0')
                if currNum <= k:
                    ans += helper(j+1)
                else:
                    break
            
            ans %= 1000000007
            dp[i] = ans
            return dp[i]
        
        n = len(s)
        dp = [-1]*n
        return helper(0)