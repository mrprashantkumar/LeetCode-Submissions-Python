class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        side = -1
        nums.sort()
        
        s = 0
        res = 0
        for i, x in enumerate(nums):
            if i >= 2:
                if s > x:
                    side = max(side, i+1)
                    res = s+x
            s += x
        
        return res if side != -1 else -1