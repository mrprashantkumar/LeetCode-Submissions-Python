class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        d = Counter()
        left = 0
        for right in range(n):
            d[nums[right]] += 1
            while d[nums[right]] > k:
                d[nums[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans