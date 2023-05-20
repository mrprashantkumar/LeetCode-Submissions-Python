class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def getans(start, end):
            visited.add(start)
            prod = 0
            for nei, wt in graph[start]:
                if nei in visited:
                    continue

                if nei == end:
                    return wt
                else:
                    smans = getans(nei, end)
                    if smans:
                        prod = wt*smans
                        break
            return prod
        
        graph = defaultdict(list)
        for (i, j), wt in zip(equations, values):
            graph[i].append((j, wt))
            graph[j].append((i, 1/wt))
        
        
        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1)
            elif a == b:
                ans.append(1)
            else:
                visited = set()
                val = getans(a, b)
                if val == 0:
                    ans.append(-1)
                else:
                    ans.append(val)
        return ans