class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        ans=0
        prefSum = 0
        for i in nums:
            prefSum += i
            if prefSum-k in d:
                ans += d[prefSum-k]
            
            d[prefSum] = d.get(prefSum, 0)+1
        
        return ans