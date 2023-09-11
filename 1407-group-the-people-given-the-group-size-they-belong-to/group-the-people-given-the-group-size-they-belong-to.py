class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        graph = defaultdict(list)
        for i, x in enumerate(groupSizes):
            graph[x].append(i)
        
        ans = []
        for size in graph:
            l = len(graph[size])
            for a in range(0, l, size):
                ans.append(graph[size][a:a+size])
        return ans