class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        val = max(nums)
        n = len(nums)
        d = Counter()
        ans = 0
        left = 0
        for right in range(n):
            d[nums[right]] += 1
            while d[val] >= k:
                d[nums[left]] -= 1
                left += 1
            
            ans += left
        return ans