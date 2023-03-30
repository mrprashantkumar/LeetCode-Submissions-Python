#User function Template for python3
from collections import *
from typing import List
import sys
sys.setrecursionlimit(10**9)
class Solution:    
    def eventualSafeNodes(self, N : int, adj : List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node in range(N):
            for nei in adj[node]:
                graph[nei].append(node)
        
        indeg = [0]*N
        for i in range(N):
            for node in graph[i]:
                indeg[node] += 1
        
        qu = deque()
        for i in range(N):
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
        return sorted(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends