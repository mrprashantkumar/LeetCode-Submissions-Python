class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suff = [0]*n
        
        suff[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i]*suff[i+1]
        suff.append(1)
        
        
        ans = []
        prodSoFar = 1
        for i in range(n):
            ans.append(prodSoFar*suff[i+1])
            prodSoFar*=nums[i]
        
        return ans