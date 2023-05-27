class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        seen = []
        curr = 0
        for i in nums:
            if not seen:
                curr += 1
                seen.append(i)
            elif seen[-1] < i:
                seen.append(i)
                curr += 1
            else:
                seen = [i]
                ans = max(ans, curr)
                curr = 1
        ans = max(ans, curr)
        return ans