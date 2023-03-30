#User function Template for python3
from collections import *
class Solution:
    def findOrder(self, N, m, prerequisites):
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)
        
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
        
        if len(ans) == N:
            return ans
        else:
            return []


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends