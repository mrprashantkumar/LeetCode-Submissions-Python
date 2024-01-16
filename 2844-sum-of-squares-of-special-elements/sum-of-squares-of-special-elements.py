class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(x*x for i, x in enumerate(nums) if n%(i+1) == 0)