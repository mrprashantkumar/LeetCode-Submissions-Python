class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if not nums:
                res.append(path)
            
            n = len(nums)
            for i in range(n):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        
        res = []
        dfs(nums, [])
        return res