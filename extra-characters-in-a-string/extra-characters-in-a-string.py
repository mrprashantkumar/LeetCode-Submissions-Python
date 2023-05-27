class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def helper(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            ans = 1 + helper(i+1)
            for j in range(1, n-i+1):
                st = s[i:i+j]
                if st in words:
                    ans = min(ans, helper(i+j))
            
            dp[i] = ans
            return ans
        n = len(s)
        dp = [-1]*(n+1)
        words = set(dictionary)
        return helper(0)