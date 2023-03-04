class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        mini, maxi, left = -1, -1, -1
        ans = 0
        
        for i,x in enumerate(nums):
            if x <= maxK and x >= minK:
                mini = i if x == minK else mini
                maxi = i if x == maxK else maxi
                ans += max(0, min(maxi, mini) - left)
            else:
                mini, maxi, left = -1, -1, i
        return ans