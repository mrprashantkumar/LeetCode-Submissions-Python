class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        ans = 0
        while k and chalk[ans] <= k:
            k -= chalk[ans]
            ans += 1
        return ans