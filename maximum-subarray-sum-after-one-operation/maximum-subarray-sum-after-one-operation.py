class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        suff = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suff[i] = max(0, nums[i]+suff[i+1])
        
        pref = 0
        ans = 0
        for i in range(n):
            ans = max(ans, pref + nums[i]*nums[i] + suff[i+1])
            pref = max(0, pref+nums[i])

        return ans
