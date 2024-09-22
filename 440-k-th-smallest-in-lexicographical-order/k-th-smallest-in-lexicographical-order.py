class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getSteps(x):
            res = 0
            diff = 1
            while x <= n:
                res += min(diff, n-x+1)
                x *= 10
                diff *= 10
            return res

        ans = 1
        while k > 1:
            steps = getSteps(ans)
            if k > steps:
                k -= steps
                ans += 1
            else:
                k -= 1
                ans *= 10
        return ans