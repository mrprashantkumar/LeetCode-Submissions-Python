class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        while i<n:
            c1, c2 = 0, 0
            while i<n and s[i] == '0':
                i += 1
                c1 += 1
            while i<n and s[i] == '1':
                c2 += 1
                i += 1
            ans = max(ans, min(c1, c2)*2)
        
        return ans
        
        