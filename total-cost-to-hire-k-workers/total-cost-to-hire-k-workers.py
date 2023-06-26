class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left, right = costs[:candidates], costs[max(candidates, n-candidates):]
        heapq.heapify(left)
        heapq.heapify(right)
        low, high = candidates, n-candidates-1
        ans = 0
        for _ in range(k):
            if not right or left and left[0] <= right[0]:
                ans += heappop(left)
                if low <= high:
                    heappush(left, costs[low])
                    low += 1
            else:
                ans += heappop(right)
                if low <= high:
                    heappush(right, costs[high])
                    high -= 1
        return ans