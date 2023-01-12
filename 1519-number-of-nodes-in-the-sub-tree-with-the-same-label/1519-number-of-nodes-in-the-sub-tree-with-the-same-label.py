class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def helper(root, par):
            d = defaultdict(int)
            for child in graph[root]:
                if child != par:
                    d1 = helper(child, root)
                    for i in d1:
                        d[i] += d1[i]
            
            d[labels[root]] += 1
            ans[root] = d[labels[root]]
            return d
        
        ans = [1]*n
        helper(0, -1)
        return ans