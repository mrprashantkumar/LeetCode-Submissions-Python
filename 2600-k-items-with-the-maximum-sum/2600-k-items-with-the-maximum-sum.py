class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        ans += min(k, numOnes)
        k -= min(k, numOnes)
        ans += min(k, numZeros)*0
        k -= min(k, numZeros)
        ans += min(k, numNegOnes)*-1
        k -= min(k, numNegOnes)
        return ans
        