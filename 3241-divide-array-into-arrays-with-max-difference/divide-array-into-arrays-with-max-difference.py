class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        ans = []
        for i in range(1, n, 3):
            if nums[i+1] - nums[i-1] > k:
                return []
            ans.append([nums[i-1], nums[i], nums[i+1]])
        return ans