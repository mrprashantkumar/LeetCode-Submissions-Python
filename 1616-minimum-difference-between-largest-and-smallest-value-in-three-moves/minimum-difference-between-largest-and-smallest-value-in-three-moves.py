class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        k = n-4
        ans = inf
        for i in range(4):
            ans = min(ans, nums[i+k] - nums[i])
        return ans