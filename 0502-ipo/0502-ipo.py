class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        nums = sorted([(i, j) for (i, j) in zip(capital, profits)])
        heap = []
        
        curr = 0
        for i in range(k):
            while curr<n and nums[curr][0] <= w:
                heappush(heap, -nums[curr][1])
                curr += 1
            if not heap:
                break
            
            w += -heappop(heap)
        
        return w