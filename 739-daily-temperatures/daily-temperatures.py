class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        ans=[0]*n
        
        seen=[]
        for i, x in enumerate(t):
            while seen and t[seen[-1]] < x:
                p = seen.pop()
                ans[p] = i-p
            
            seen.append(i)
        return ans