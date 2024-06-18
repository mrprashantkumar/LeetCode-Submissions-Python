class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs = sorted(zip(difficulty, profit))
        worker.sort()
        n, m = len(profit), len(worker)
        heap = []
        ans = 0
        i = w = 0
        c = 0
        while i < n and w < m:
            while i < n and pairs[i][0] <= worker[w]:
                heappush(heap, -pairs[i][1])
                i += 1
            
            if heap:
                ans += -heap[0]
                c += 1
            w += 1
        
        while w < m and heap:
            ans += -heap[0]
            w += 1

        return ans