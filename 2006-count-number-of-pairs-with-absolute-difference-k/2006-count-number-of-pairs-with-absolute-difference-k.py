class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0
        
        for i in d:
            if i-k in d:
                ans += (d[i]*d[i-k])
        
        return ans