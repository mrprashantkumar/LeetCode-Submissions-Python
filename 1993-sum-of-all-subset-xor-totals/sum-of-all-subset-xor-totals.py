class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @cache
        def helper(i, x):
            if i == n:
                return x
            
            notTake = helper(i+1, x)
            take = helper(i+1, nums[i] ^ x)

            return take + notTake
        
        n = len(nums)
        return helper(0, 0)