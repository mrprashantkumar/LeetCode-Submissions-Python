class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n, m = len(s1), len(s2)
        for i in range(m-n+1):
            if s1 == sorted(s2[i:i+n]):
                return True
        return False