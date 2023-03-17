class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            return n-min(right)
        if not right:
            return max(left)
        ans1, ans2 = n-min(right), max(left)
        return max(ans1, ans2)