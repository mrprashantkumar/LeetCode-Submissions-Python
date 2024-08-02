class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        totalOnes = nums.count(1)
        nums += nums

        oneCount = 0
        for i in range(totalOnes-1):
            if nums[i] == 1:
                oneCount += 1
        
        ans = n
        for i in range(totalOnes-1, n+totalOnes-1):
            if nums[i] == 1:
                oneCount += 1
            
            ans = min(ans, totalOnes - oneCount)

            if nums[i - totalOnes + 1] == 1:
                oneCount -= 1
        
        return ans