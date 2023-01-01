class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        n = len(pattern)
        if n != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False
        
        d={}
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = pattern[i]
            elif d[s[i]] != pattern[i]:
                return False
        return True
                    