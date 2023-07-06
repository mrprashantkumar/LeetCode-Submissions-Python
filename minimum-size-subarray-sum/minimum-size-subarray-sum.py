class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, 1
        windowSum = nums[0]
        ans = 1000000007
        while high < n:
            if windowSum >= target:
                while windowSum >= target:
                    ans = min(ans, high-low)
                    windowSum -= nums[low]
                    low += 1
            else:
                windowSum += nums[high]
                high += 1
        while windowSum >= target:
            ans = min(ans, high-low)
            windowSum -= nums[low]
            low += 1
        return ans if ans != 1000000007 else 0