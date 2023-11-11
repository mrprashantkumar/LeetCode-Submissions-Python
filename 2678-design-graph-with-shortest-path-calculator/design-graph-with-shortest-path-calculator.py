class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for i, j, wt in edges:
            self.graph[i].append((j, wt))
            

    def addEdge(self, edge: List[int]) -> None:
        i, j, wt = edge
        self.graph[i].append((j, wt))
        

    def shortestPath(self, src: int, dst: int) -> int:
        ans = [1000000007]*self.n
        ans[src] = 0
        qu = [(0, src)]
        while qu:
            x, curr = qu.pop()
            for nei, wt in self.graph[curr]:
                if ans[nei] > ans[curr]+wt:
                    ans[nei] = ans[curr]+wt
                    heapq.heappush(qu, (ans[nei], nei))
        return ans[dst] if ans[dst] != 1000000007 else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)