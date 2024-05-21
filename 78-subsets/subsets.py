class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, subset):
            if i == n:
                self.ans.append(subset)
                return 

            helper(i+1, subset)
            helper(i+1, subset+[nums[i]])
            return
        
        n = len(nums)
        self.ans = []
        helper(0, [])
        return self.ans