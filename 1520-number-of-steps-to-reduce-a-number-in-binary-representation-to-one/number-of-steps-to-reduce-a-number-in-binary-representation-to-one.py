class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        pow = 0
        while s:
            num += 2**pow * int(s[-1])
            pow += 1
            s = s[:-1]
            
        ans = 0
        while num != 1:
            if num&1:
                num += 1
            else:
                num //= 2
            ans += 1
        return ans