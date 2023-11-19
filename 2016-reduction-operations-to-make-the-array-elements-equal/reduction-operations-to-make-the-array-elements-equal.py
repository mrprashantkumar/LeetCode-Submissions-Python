class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mini = nums[0]
        ans = 0
        for i in range(n):
            if nums[i] != mini:
                mini = nums[i]
                ans += (n-i)
        return ans