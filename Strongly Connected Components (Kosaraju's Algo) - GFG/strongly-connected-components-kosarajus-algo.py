#User function Template for python3
class Solution:
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        def dfs1(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs1(nei)
            
            
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
            nodes.append(node)
        
        # print(adj)
        visited = set()
        nodes = []
        for i in range(V):
            if i not in visited:
                dfs(i)
                
        graph = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                graph[v].append(u)
        # print(graph)
        
        ans = 0
        visited = set()
        for i in nodes[::-1]:
            if i not in visited:
                dfs1(i)
                ans += 1
        
        return ans
    
    
    
    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
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
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends