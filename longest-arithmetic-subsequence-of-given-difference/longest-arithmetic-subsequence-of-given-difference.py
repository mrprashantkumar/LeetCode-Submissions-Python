class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        diff = {}
        for i in nums:
            if i-difference in diff:
                diff[i] = diff[i-difference] + 1
            else:
                diff[i] = 1
        return max(diff.values())