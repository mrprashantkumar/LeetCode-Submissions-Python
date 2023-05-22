class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i for i, j in intervals]
        end = [j for i, j in intervals]
        start.sort()
        end.sort()
        n = len(start)

        ans = 0
        i, j = 0, 0
        while i<n:
            if start[i] < end[j]:
                ans += 1
            else:
                j += 1
            i += 1
        return ans