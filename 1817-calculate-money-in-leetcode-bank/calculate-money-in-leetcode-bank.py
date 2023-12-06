class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        day = 1
        money = 1
        while day <= n:
            curr = money
            while day <= n and (curr - money) < 7:
                ans += curr
                curr += 1
                day += 1
            money += 1
        return ans