class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, arraySoFar):
            ans.append(arraySoFar)
            
            for j in range(i, n):
                if i == j or nums[j] != nums[j-1]:
                    helper(j+1, arraySoFar+[nums[j]])
            
            return

        n = len(nums)
        nums.sort()
        ans = []
        helper(0, [])
        return ans