class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(list)
        outdeg = [0]*n
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            outdeg[i] += 1
            outdeg[j] += 1
        
        ans = deque()
        for i in range(n):
            if outdeg[i] == 1:
                ans.append(i)
        
        nodesLeft = n
        while nodesLeft > 2:
            l = len(ans)
            nodesLeft -= l
            for _ in range(l):
                curr = ans.popleft()
                for nei in graph[curr]:
                    outdeg[nei] -= 1
                    if outdeg[nei] == 1:
                        ans.append(nei)
        return ans