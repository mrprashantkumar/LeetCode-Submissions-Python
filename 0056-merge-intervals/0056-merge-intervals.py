class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans=[]
        for i in intervals:
            if ans and ans[-1][1] >= i[0]:
                ans[-1][1] = max(i[1], ans[-1][1])
            else:
                ans.append(i)
        return ans