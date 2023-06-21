class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = [[i, j] for i, j in zip(nums, cost)]
        pairs.sort()
        n = len(nums)

        pref = [0]*n
        pref[0] = pairs[0][1]
        for i in range(1, n):
            pref[i] = pairs[i][1] + pref[i-1]
        
        totalCost = 0
        for i in range(n):
            totalCost += pairs[i][1]*(pairs[i][0] - pairs[0][0])
        
        ans = totalCost
        for i in range(1, n):
            gap = pairs[i][0] - pairs[i-1][0]
            totalCost += gap * pref[i-1]
            totalCost -= gap * (pref[n-1] - pref[i-1])
            ans = min(ans, totalCost)
        return ans