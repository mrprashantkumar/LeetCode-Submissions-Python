class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while i<n:
            if nums[i]&1 == 0 and nums[i] <= threshold:
                c = 1
                seen = [nums[i]]
                i += 1
                while i < n and nums[i]&1 != seen[-1]&1 and nums[i] <= threshold:
                    seen.append(nums[i])
                    i += 1
                    c += 1
                ans = max(ans, c)
            else:
                i += 1
        return ans