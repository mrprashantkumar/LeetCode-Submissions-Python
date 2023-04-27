class Solution:
    def bulbSwitch(self, n: int) -> int:
        ans = 0
        i = 1
        while i*i <= n:
            ans += 1
            i += 1
        return ans
        