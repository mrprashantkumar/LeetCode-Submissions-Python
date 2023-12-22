class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        ans, zero = 0, 0
        for i in range(n-1):
            if s[i] == '0':
                zero += 1
            else:
                ones -= 1
            ans = max(ans, zero + ones)
        return ans