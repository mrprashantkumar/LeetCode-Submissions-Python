class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            vc, cc = 0, 0
            for j in range(i, n):
                if s[j] in 'aeiou':
                    vc += 1
                else:
                    cc += 1
                
                if vc == cc and vc*cc % k == 0:
                    ans += 1
        return ans