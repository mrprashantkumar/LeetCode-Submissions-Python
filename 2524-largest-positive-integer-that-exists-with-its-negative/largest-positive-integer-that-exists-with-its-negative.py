class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        
        for i in reversed(sorted(nums)):
            if -i in nums:
                return i
        
        return -1