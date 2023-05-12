class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        n, m = len(s), len(t)
        
        if n < m:
            for i in range(m):
                if t[:i]+t[i+1:] == s:
                    return True
        elif n > m:
            for i in range(n):
                if s[:i]+s[i+1:] == t:
                    return True
        else:
            for i in range(n):
                if s[:i]+s[i+1:] == t[:i]+t[i+1:]:
                    return True
        return False