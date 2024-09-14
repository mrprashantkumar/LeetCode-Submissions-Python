class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        curr_count = 0
        ans = 0
        for i in nums:
            if i == maxi:
                curr_count += 1
            else:
                curr_count = 0
            
            ans = max(ans, curr_count)
        return ans