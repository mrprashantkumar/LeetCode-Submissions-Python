class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(i,subsequence):
            if len(subsequence)>1:
                ans.add(tuple(subsequence))
            if i==n:
                return
            
            if not subsequence or nums[i] >= subsequence[-1]:
                helper(i+1, subsequence+[nums[i]]) 
            helper(i+1, subsequence)
        
        ans = set()
        n = len(nums)
        helper(0,[])
        return ans