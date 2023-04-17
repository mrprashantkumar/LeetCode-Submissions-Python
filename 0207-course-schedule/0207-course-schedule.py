class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for i, j in prerequisites:
            graph[i].append(j)
            indeg[j] += 1
        
        qu = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                qu.append(i)
        
        count = 0
        while qu:
            curr = qu.popleft()
            count += 1
            for nei in graph[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
        
        return count == numCourses