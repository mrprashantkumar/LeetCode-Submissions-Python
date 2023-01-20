class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        n = len(s)
        l=0

        for i in range(n):
            if s[i] in seen:
                l = max(seen[s[i]], l)
            ans = max(ans, i-l+1)
            seen[s[i]] = i+1
        return ans