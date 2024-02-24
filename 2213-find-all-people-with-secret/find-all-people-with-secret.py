class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(lambda : defaultdict(set))

        for x, y, time in meetings:
            graph[time][x].add(y)
            graph[time][y].add(x)
        
        ans = {0, firstPerson}

        for t in sorted(graph):
            def dfs(node):
                ans.add(node)
                for nei in graph[t][node] - ans:
                    dfs(nei)

            for curr in graph[t].keys() & ans:
                dfs(curr)
        
        return ans