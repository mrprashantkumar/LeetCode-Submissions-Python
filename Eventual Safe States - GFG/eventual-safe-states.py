#User function Template for python3

from typing import List
import sys
sys.setrecursionlimit(10**9)
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        def dfs(node):
            visited.add(node)
            seen.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in seen:
                    return True
            seen.remove(node)
            ans.append(node)
            return False
        
        visited = set()
        seen = set()
        ans = []
        for i in range(V):
            if i not in visited:
                dfs(i)
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