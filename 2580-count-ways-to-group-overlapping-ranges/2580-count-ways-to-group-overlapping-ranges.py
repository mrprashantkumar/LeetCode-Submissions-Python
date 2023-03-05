class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        ans = 1
        right = -1
        
        for i, j in ranges:
            if right < i:
                ans *= 2
                ans %= 1000000007
            right = max(right, j)
        
        return ans