class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        pref = 0
        for i, x in enumerate(nums):
            pref += x
            ans = max(ans, (pref+i)//(i+1))
        return ans