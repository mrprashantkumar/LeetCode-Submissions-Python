class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        d = {}
        for i, x in enumerate(s):
            if x in d:
                ans = max(ans, i-d[x]-1)
            else:
                d[x] = i
        return ans