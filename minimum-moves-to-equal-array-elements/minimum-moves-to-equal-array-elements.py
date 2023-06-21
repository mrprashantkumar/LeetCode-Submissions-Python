class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ele = min(nums)
        ans = 0
        for i in nums:
            ans += abs(i-ele)
        return ans