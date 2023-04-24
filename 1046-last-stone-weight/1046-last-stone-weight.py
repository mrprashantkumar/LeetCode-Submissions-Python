import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if x!=y:
                item = y-x
                stones.append(item)
                heapq._heapify_max(stones)
        
        return stones[0] if stones else 0