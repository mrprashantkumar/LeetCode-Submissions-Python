class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0]*(n+1)
        outdeg = [0]*(n+1)
        
        for i, j in trust:
            indeg[i] += 1
            outdeg[j] += 1
        
        for i in range(1,n+1):
            if indeg[i] == 0 and outdeg[i]==n-1:
                return i
        return -1