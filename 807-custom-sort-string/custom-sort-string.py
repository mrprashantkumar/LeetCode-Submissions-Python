class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(s, key = lambda x : order.index(x) if x in order else 27))