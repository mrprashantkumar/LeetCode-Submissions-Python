class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n):
            if n%i == 0:
                if s[:i]*(n//i) == s:
                    return True
        return False