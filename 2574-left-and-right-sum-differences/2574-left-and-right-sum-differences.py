class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suff = [0]*(n)
        
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1]+nums[i+1]
        
        ans = [0]*(n)
        pref = 0
        for i in range(n):
            ans[i] = abs(pref-suff[i])
            pref += nums[i]
        
        return ans