class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        i = 1
        r = 1
        while i <= n:
            c = r
            while i <= n and (c-r) < 7:
                ans += c
                c += 1
                i += 1
            r += 1
        return ans