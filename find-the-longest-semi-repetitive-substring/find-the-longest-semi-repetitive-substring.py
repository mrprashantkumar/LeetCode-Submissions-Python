class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def check(st):
            k = len(st)
            c = 0
            for a in range(k-1):
                if st[a] == st[a+1]:
                    c += 1
            return c <= 1
        
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if check(s[i:j+1]):
                    ans = max(ans, len(s[i:j+1]))
        return ans
