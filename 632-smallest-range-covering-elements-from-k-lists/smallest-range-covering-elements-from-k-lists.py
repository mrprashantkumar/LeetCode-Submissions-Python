class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        qu = []
        maxi = -float("inf")
        resStart, resEnd = 0, float("inf")

        for i in range(k):
            heappush(qu, (nums[i][0], i, 0))
            maxi = max(maxi, nums[i][0])
        
        lenQu = k
        while lenQu == k:
            mini, ind, col = heappop(qu)
            lenQu -= 1
            if abs(mini - maxi) < abs(resStart - resEnd):
                resStart = mini
                resEnd = maxi
            
            if col+1 < len(nums[ind]):
                heappush(qu, (nums[ind][col+1], ind, col+1))
                maxi = max(maxi, nums[ind][col+1])
                lenQu += 1
            
        return [resStart, resEnd]
