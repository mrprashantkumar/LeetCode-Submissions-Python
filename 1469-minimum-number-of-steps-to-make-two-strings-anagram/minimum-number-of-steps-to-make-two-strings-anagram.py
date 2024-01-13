class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1, d2 = Counter(s), Counter(t)
        ans = 0
        for i in range(97, 97+26):
            ans += max(0, d2[chr(i)] - d1[chr(i)])
        return ans