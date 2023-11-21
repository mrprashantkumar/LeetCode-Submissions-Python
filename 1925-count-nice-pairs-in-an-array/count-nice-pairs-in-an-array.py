class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            res = 0
            while num:
                res *= 10
                res += num%10
                num //= 10
            return res
        

        d = Counter()
        ans = 0
        for i in nums:
            val = i - rev(i)
            if val in d:
                ans += d[val]
                ans %= 1000000007
            d[val] += 1
        return ans