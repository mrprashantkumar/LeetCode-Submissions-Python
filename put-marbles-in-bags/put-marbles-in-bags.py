class Solution:
    def putMarbles(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k==1 or k==n:
            return 0
        
        seen = []
        for i in range(n-1):
            seen.append(nums[i]+nums[i+1])
        
        seen.sort()
        return abs(sum(seen[:k-1])- sum(seen[-k+1:]))