class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n+1):
            ind = bisect_left(nums, i)
            if (n - ind) == i:
                return i
        
        return -1