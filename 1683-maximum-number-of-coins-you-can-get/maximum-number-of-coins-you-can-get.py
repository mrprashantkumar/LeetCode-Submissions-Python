class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)

        ans = 0
        for i in range(n-2, n//3 -1, -2):
            ans += piles[i]
        return ans