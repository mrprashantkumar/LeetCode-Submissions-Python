class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        qu = []
        n = len(heights)

        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                continue
            
            heappush(qu, diff)
            if len(qu) > ladders:
                bricks -= heappop(qu)
            if bricks < 0:
                return i-1

        return n-1