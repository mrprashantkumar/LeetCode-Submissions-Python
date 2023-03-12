class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        low, high = 0, len(nums)-1
        
        while low<high:
            ps = nums[low]+nums[high]
            if ps == k:
                ans += 1
                low += 1
                high -= 1
            elif ps > k:
                high -= 1
            else:
                low += 1
        return ans