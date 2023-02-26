class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums)%p
        if rem==0:
            return 0
        pref = 0
        d = {0:-1}
        ans = n = len(nums)
        for i, x in enumerate(nums):
            pref += x
            pref %= p
            d[pref] = i
            if (pref-rem)%p in d:
                ans = min(ans, i-d[(pref-rem)%p])
        
        return ans if ans < n else -1