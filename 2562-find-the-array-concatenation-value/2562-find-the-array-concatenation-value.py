class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        ans = 0
        
        while low<high:
            ans += nums[high]
            l = len(str(nums[high]))
            ans += nums[low]*(10**l)
            
            low += 1
            high -= 1
        if low==high:
            ans += nums[low]
        return ans