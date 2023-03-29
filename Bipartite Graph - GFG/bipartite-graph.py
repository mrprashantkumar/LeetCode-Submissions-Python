from collections import *
class Solution:
	def isBipartite(self, V, adj):
	    def dfs(node, color):
	        visited[node] = color
            for nei in adj[node]:
                if visited[nei] == -1:
                    if not dfs(nei, 1-color):
                        return False
                elif visited[nei] == color:
                    return False
            return True
	    
	    visited = [-1]*(V)
	    for i in range(V):
	        if visited[i] == -1:
	            if not dfs(i, 0):
	                return False
	    return True
		#code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends