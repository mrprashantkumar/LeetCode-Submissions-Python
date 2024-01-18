class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        @cache
        def helper(i, par):
            if i == n:
                return 0
            
            notTake = helper(i+1, par)
            take = helper(i+1, nums[i]&1) + nums[i]
            if nums[i]&1 != par:
                take -= x
            
            return max(take, notTake)
        
        n = len(nums)
        return helper(0, nums[0]&1)