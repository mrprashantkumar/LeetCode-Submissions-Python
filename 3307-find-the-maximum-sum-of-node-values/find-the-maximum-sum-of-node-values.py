class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        @cache
        def helper(i, isEven):
            if i == n:
                return 0 if isEven == 1 else -inf
            
            notTake = nums[i] + helper(i+1, isEven)
            take = (nums[i] ^ k) + helper(i+1, 1 - isEven)

            return max(take, notTake)
        
        n = len(nums)
        return helper(0, 1)