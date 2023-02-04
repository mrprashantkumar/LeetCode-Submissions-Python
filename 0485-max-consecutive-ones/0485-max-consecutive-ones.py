class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in nums:
            if i==1:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 0
        ans = max(ans, curr)
        return ans
            