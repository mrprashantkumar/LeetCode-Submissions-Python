class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumsofar = 0
        ans = 0
        d = {}
        
        for i in nums:
            sumsofar += i
            if sumsofar == k:
                ans += 1
            
            if sumsofar-k in d:
                ans += d[sumsofar-k]
            d[sumsofar] =  d.get(sumsofar, 0) + 1
        return ans
            
            