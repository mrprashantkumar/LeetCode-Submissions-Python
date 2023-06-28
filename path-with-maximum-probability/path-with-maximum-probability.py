class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (i, j), wt in zip(edges, succProb):
            graph[i].append((j, wt))
            graph[j].append((i, wt))
        
        ans = [0]*n
        ans[start] = 1

        qu = [(-1, start)]
        while qu:
            val, curr = heappop(qu)

            if curr == end:
                return -val
            
            for nei, wt in graph[curr]:
                if -val * wt > ans[nei]:
                    ans[nei] = -val * wt
                    heappush(qu, (-ans[nei], nei))
        return 0