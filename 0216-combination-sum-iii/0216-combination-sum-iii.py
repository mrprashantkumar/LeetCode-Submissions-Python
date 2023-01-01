class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(num, path, target, k):
            if k==0:
                if target==0:
                    ans.append(path)
                return 
            
            
            for i in range(num, 10):
                helper(i+1, path+[i], target-i, k-1)
        
        ans = []
        helper(1, [], n, k)
        return ans