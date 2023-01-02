class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sumArray = sum(nums)
        curr = sum([i*x for i, x in enumerate(nums)])
        
        ans = curr
        for i in range(1, n):
            curr += (sumArray - nums[-i]*n)
            ans = max(ans, curr)
        return ans