class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        ans = 0
        for i, j in zip(s, s[1::]):
            if i != j:
                ans += 1
        return ans