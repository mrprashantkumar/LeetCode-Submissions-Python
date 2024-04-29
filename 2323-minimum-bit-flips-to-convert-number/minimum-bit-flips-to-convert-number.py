class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        val = start ^ goal
        ans = 0
        while val:
            ans += val&1
            val //= 2
        return ans