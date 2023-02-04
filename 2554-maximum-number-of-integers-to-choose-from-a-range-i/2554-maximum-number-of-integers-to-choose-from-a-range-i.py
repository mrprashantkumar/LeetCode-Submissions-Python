class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen = set(banned)
        ans = 0
        for i in range(1, n+1):
            if i not in seen and i<=maxSum:
                ans += 1
                maxSum -= i
        return ans
                