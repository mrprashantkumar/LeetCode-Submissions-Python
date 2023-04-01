#User function Template for python3
from collections import *
class Solution:
    def shortestPath(self, edges, n, m, src):
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        qu = deque([src])
        ans = [1000000007]*n
        ans[src] = 0
        
        visited = set()
        dist = 1
        while qu:
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                for nei in graph[curr]:
                    visited.add(curr)
                    ans[nei] = min(ans[nei], dist)
                    if nei not in visited:
                        qu.append(nei)
            
            dist += 1
        for i in range(n):
            if ans[i] == 1000000007:
                ans[i] = -1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends