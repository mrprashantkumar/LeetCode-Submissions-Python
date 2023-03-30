#User function Template for python3
from collections import *
import sys
sys.setrecursionlimit(10**6)
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        indeg = [0]*V
        for i in range(V):
            for node in adj[i]:
                indeg[node] += 1
        
        qu = deque()
        for deg in range(V):
            if indeg[deg] == 0:
                qu.append(deg)
        
        ans = []
        while qu:
            curr = qu.popleft()
            ans.append(curr)
            for nei in adj[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
                    
        return len(ans) != V


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends