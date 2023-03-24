#User function Template for python3

from typing import List
from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, graph: List[List[int]]) -> List[int]:
        ans = []
        qu = deque([0])
        visited = set()
        visited.add(0)
        while qu:
            curr = qu.popleft()
            ans.append(curr)
            
            for node in graph[curr]:
                if node not in visited:
                    visited.add(node)
                    qu.append(node)
        
        return ans


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends