class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        d[0] = -1
        pref = 0
        ans = 0
        for i, x in enumerate(nums):
            if x == 1:
                pref += 1
            else:
                pref -= 1
            
            if pref in d:
                ans = max(ans, i - d[pref])
            else:
                d[pref] = i
        return ans