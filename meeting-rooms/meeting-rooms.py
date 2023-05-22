class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n = len(intervals)
        for i in range(n-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True