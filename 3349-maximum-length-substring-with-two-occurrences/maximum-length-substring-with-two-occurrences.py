class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        d = Counter()
        left, n = 0, len(s)
        for right in range(n):
            d[s[right]] += 1
            while max(d.values()) > 2:
                d[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans