#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, graph):
        qu = []
        heapq.heappush(qu, (0, 0, -1))
        visited = set()
        ans = 0
        
        while qu:
            wt, curr, parent = heapq.heappop(qu)
            if curr not in visited:
                if parent != -1 and curr not in visited:
                    ans += wt
                visited.add(curr)
                for nei, nwt in graph[curr]:
                    if nei not in visited:
                        heapq.heappush(qu, (nwt, nei, curr))
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends