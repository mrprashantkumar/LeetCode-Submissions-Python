class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1]*n
        
        lis = []
        
        for i, x in enumerate(obstacles):
            ind =  bisect_right(lis, x)
            
            if ind == len(lis):
                lis.append(x)
            else:
                lis[ind] = x
            
            ans[i] = ind+1
        return ans