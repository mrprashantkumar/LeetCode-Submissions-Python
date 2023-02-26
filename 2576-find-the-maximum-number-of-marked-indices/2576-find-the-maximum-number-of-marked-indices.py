class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i, j, count = 0, (n+1)//2, 0
        while i<j and j < n:
            if 2 * nums[i] <= nums[j]:
                count += 2
                i += 1
                j += 1
            else:
                j += 1
            
        return count