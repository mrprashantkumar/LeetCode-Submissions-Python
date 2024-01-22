class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(set(nums))
        dup = sum(nums)-s
        mis = n*(n+1)//2 - s
        return [dup, mis]