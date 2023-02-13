class Solution:
    def countOdds(self, low: int, high: int) -> int:
        maxi = (high+1)//2
        mini = low//2
        return maxi-mini