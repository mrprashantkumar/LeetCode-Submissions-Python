class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        seen = []
        curr = 0
        for i in nums:
            if not seen or seen[-1] < i:
                seen.append(i)
                curr += i
            else:
                seen = [i]
                ans = max(ans, curr)
                curr = i
        ans = max(ans, curr)
        return ans