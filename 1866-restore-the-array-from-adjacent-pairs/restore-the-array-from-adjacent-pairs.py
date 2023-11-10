class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(node):
            visited.add(node)
            self.ans.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
            return 

        count = Counter()
        graph = defaultdict(list)
        for i, j in adjacentPairs:
            count[i] += 1
            count[j] += 1
            graph[i].append(j)
            graph[j].append(i)
        
        self.ans = []
        visited = set()
        for i in count:
            if count[i] == 1:
                dfs(i)
                break
        return self.ans
        
