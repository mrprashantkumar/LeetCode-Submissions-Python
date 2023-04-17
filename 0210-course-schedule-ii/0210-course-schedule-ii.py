class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for i, j in prerequisites:
            graph[i].append(j)
            indeg[j] += 1
        
        qu = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                qu.append(i)
        
        ans = []
        while qu:
            curr = qu.popleft()
            ans.append(curr)
            for nei in graph[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
        
        return ans[::-1] if len(ans) == numCourses else []