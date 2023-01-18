class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        arrSum = 0
        maxSum, curMax = nums[0], 0
        minSum, curMin = nums[0], 0
        
        for i in nums:
            arrSum += i
            curMax = max(curMax+i, i)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin+i, i)
            minSum = min(minSum, curMin)
            
        return max(maxSum, arrSum-minSum) if maxSum>0 else maxSum