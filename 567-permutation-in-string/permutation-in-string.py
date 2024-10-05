class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        d1 = {}
        for i in s1:
            d1[i] = d1.get(i, 0) + 1
        
        d2 = {}
        for right in range(n-1):
            d2[s2[right]] = d2.get(s2[right], 0) + 1
        
        left = 0
        for right in range(n-1, m):
            d2[s2[right]] = d2.get(s2[right], 0) + 1
            if d1 == d2:
                return True
            d2[s2[left]] -= 1
            if d2[s2[left]] == 0:
                del d2[s2[left]]
            left += 1
        
        return False