class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        count1 = s.count("1")
        left = 0
        right = n-count1
        ans = left+right
        for i in range(n):
            if s[i]=='0':
                right -= 1
            else:
                left += 1
            ans = min(ans, left+right)
        return ans