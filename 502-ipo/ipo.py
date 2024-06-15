class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pair = sorted([(i, j) for (i, j) in zip(capital, profits)])
        heap = []
        
        i = 0
        while k:
            while i < n and pair[i][0] <= w:
                heappush(heap, -pair[i][1])
                i += 1
                
            if not heap:
                break
            
            w += -heappop(heap)
            k -= 1
        
        return w