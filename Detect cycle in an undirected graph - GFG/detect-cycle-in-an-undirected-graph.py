from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, graph: List[List[int]]) -> bool:
        def bfs(node, parent):
            qu = deque([(node, parent)])
            
            while qu:
                curr, parent = qu.popleft()
                visited.add(curr)
                for child in graph[curr]:
                    if child != parent:
                        if child in visited:
                            return True
                        else:
                            qu.append((child, curr))
            return False
        
        visited = set()
        for i in range(V):
            if i not in visited:
                if bfs(i, -1):
                    return True
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends