class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sumArray = 0
        curr = 0
        
        for i in range(n):
            sumArray += nums[i]
            curr += i*nums[i]
        
        ans = curr
        for i in range(1, n):
            curr += (sumArray - nums[-i]*n)
            ans = max(ans, curr)
        return ans