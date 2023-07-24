class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(i):
            if i == 0:
                return 1
            if i == 1:
                return x
            
            if i&1:
                ans = x
            else:
                ans = 1

            halfpower = helper(i//2)
            ans *= halfpower
            ans *= halfpower
            return ans
            
        res = helper(abs(n))
        if n >= 0:
            return res
        else:
            return 1/res