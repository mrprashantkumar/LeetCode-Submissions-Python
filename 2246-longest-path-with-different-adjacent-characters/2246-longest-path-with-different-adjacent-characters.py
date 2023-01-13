class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = [[] for i in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)
        
        def helper(node):
            if len(graph[node]) == 0:
                return 1
            first, sec = 0, 0
            for child in graph[node]:
                a1 = helper(child)
                if s[child] != s[node]:
                    if a1 >= first:
                        sec = first
                        first = a1
                    elif a1 >= sec:
                        sec = a1
                self.ans = max(self.ans, 1+first+sec)
            
            return first+1
        
        self.ans = 1
        helper(0)
        return self.ans