class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def bfs(src):
            ans = [1000000007]*n
            ans[src] = 0
            
            qu = set()
            qu.add((0, src))
            while qu:
                x, curr = qu.pop()
                for nei, wt in graph[curr]:
                    if ans[nei] > ans[curr]+wt:
                        if (ans[nei], nei) in qu:
                            qu.remove((ans[nei], nei))
                        ans[nei] = ans[curr]+wt
                        qu.add((ans[nei], nei))
            
            for node, cost in enumerate(ans):
                if cost <= distanceThreshold and node != src:
                    isReachable[src].add(node)

        graph = defaultdict(list)
        for x, y, w in edges:
            graph[x].append([y, w])
            graph[y].append([x, w])
        
        isReachable = [set() for _ in range(n)]
        for node in range(n):
            bfs(node)

        minLen = min(len(s) for s in isReachable)
        node = 0
        for i, s in enumerate(isReachable):
            if len(s) == minLen:
                node = max(node, i)
        return node