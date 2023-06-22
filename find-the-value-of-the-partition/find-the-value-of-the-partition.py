class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 1000000007
        for i in range(n-1):
            ans = min(ans, nums[i+1] - nums[i])
        return ans