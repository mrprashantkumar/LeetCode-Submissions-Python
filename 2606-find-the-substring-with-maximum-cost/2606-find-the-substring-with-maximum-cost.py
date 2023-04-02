class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        ans = 0
        d = {}
        for x, y in zip(chars, vals):
            d[x] = y
        su = 0
        for i in s:
            su += d.get(i, ord(i)-96)
            ans = max(ans, su)
            su = max(su, 0)
        return ans