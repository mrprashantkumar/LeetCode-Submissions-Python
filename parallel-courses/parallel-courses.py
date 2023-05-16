class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indeg = [0]*(n+1)
        for i, j in relations:
            graph[i].append(j)
            indeg[j] += 1
        
        qu = deque()
        for i in range(1, n+1):
            if indeg[i] == 0:
                qu.append(i)
        
        ans = 0
        count = 0
        while qu:
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                count += 1
                for nei in graph[curr]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        qu.append(nei)
            ans += 1
        return ans if count == n else -1