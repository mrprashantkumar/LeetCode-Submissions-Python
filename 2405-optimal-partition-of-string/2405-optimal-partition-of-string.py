class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        while i<n:
            seen = set()
            while i<n and s[i] not in seen:
                seen.add(s[i])
                i += 1
            
            ans += 1
        return ans