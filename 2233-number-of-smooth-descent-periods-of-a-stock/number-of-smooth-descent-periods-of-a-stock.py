class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        val = prices[0]
        curr = 1
        for i in prices[1::]:
            if i == val-1:
                val -= 1
                curr += 1
            else:
                val = i
                curr = 1
            ans += curr
        return ans