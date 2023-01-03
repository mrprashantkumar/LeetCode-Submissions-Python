class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        
        ans=0
        for j in range(m):
            for i in range(n-1):
                if strs[i][j] > strs[i+1][j]:
                    ans += 1
                    break
        
        return ans