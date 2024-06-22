class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        count = 0
        ans = 0
        for i in nums:
            if i&1:
                count += 1
            if count - k in d:
                ans += d[count - k]
            
            d[count] = d.get(count, 0) + 1
        
        return ans