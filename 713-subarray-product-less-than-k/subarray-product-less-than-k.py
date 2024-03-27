class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = 1
        ans = 0
        left = 0
        for right in range(n):
            p *= nums[right]
            while left <= right and p >= k:
                p /= nums[left]
                left += 1
            
            ans += (right - left + 1)
        return ans