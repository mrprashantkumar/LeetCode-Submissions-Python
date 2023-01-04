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
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            elif d[pattern[i]] != s[i]:
                return False
        return True
                    