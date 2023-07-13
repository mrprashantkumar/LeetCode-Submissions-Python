class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i, arraysofar):
            if i == n:
                ans.append(arraysofar[:])
                return   

            for j in range(i, n):
                arraysofar[i], arraysofar[j] = arraysofar[j], arraysofar[i]
                helper(i+1, arraysofar)
                arraysofar[i], arraysofar[j] = arraysofar[j], arraysofar[i]
            
            return
        
        n = len(nums)
        ans = []
        helper(0, nums)
        return ans