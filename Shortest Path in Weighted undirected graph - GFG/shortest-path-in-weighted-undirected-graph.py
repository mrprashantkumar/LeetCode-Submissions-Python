#User function Template for python3
from collections import *
class Solution:
    def shortestPath(self, n, m, edges):
        graph = defaultdict(list)
        for i, j, wt in edges:
            graph[i].append((j, wt))
            graph[j].append((i, wt))
        
        ans = [1000000007]*(n+1)
        ans[1] = 0
        
        dp = [0]*(n+1)
        qu = set()
        qu.add((0, 1))
        while qu:
            x, curr = qu.pop()
            for nei, wt in graph[curr]:
                if ans[nei] > ans[curr]+wt:
                    if (ans[nei], nei) in qu:
                        qu.remove((ans[nei], nei))
                    ans[nei] = ans[curr]+wt
                    dp[nei] = curr
                    qu.add((ans[nei], nei))
        # print(dp, ans)
        if ans[n] == 1000000007:
            return [-1]
        res = [n]
        node = n
        while dp[node] != 0:
            res.append(dp[node])
            node = dp[node]
        
        return res[::-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends