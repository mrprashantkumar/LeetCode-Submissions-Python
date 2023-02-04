class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        d = {}
        for i, x in enumerate(nums):
            d[x] = i
        for i, j in operations:
            ind = d[i]
            nums[ind] = j
            d[j] = ind
        return nums