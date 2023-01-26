class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = {}
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        pq = [(0, 0, src)]
        while pq:
            cost, stops, node = heapq.heappop(pq)
            if node == dst and stops - 1 <= k:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for neighbor, price in adj[node]:
                    heapq.heappush(pq, (cost + price, stops + 1, neighbor))
        return -1