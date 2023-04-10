class Solution:
    def minimumMoves(self, s: str) -> int:
        i, ans = 0, 0
        n = len(s)
        
        while i<n:
            if s[i] == 'X':
                i += 3
                ans += 1
            else:
                i += 1
        return ans