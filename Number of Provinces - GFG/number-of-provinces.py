#User function Template for python3
from collections import *
class Solution:
    def numProvinces(self, adj, n):
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if adj[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                ans += 1
                dfs(i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends