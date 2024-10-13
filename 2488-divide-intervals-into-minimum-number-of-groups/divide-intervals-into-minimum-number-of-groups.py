class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endTimes = []
        for left, right in intervals:
            if endTimes and left > endTimes[0]:
                heapq.heappop(endTimes)

            heapq.heappush(endTimes, right)

        return len(endTimes)