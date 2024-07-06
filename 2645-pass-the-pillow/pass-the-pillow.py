class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = 1
        ans = 1
        while time:
            ans += d
            time -= 1
            if time == 0:
                return ans
            if ans == n or ans == 1:
                d *= -1
        return ans