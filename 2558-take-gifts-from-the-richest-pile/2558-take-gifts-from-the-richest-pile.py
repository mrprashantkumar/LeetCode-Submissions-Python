class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq._heapify_max(gifts)
        for _ in range(k):
            heapq._heapreplace_max(gifts, int(math.sqrt(gifts[0])))
        return sum(gifts)