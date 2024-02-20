class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = len(nums)
        return i*(i+1)//2-sum(nums)