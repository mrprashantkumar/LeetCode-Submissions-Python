class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        maxi = 0
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            maxi = max(maxi, d[i])
        ans = [[] for _ in range(maxi)]
        for i in d:
            val = d[i]
            for j in range(val):
                ans[j].append(i)
        
        return ans