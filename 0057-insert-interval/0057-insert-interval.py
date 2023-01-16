class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        n = len(intervals)
        ans=[]
        for i in range(n):
            if ans and ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
        return ans