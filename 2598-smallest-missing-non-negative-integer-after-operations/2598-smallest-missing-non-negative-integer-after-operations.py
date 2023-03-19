class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = {}
        n = len(nums)
        for v in nums:
            d[v%value] = d.get(v%value, 0)+1
        
        for i in range(n+2):
            if d.get(i%value, 0) > 0:
                d[i%value] -= 1
            else:
                return i