class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(lambda : 1)
        
        for right in range(n):
            for left in range(right):
                dp[(right, nums[right] - nums[left])] = dp[(left, nums[right] - nums[left])] + 1   
        return max(dp.values())