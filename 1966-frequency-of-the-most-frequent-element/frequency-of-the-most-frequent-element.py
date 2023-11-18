class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        ans = 0
        pref = 0
        for right in range(n):
            pref += nums[right]
            while (pref + k) < (right-left+1) * nums[right]:
                pref -= nums[left]
                left += 1
            
            ans = max(ans, right-left+1)
        return ans