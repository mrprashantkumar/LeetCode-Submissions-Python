#User function Template for python3
from collections import *
class Solution:
    def isPossible(self,N,prerequisites):
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)
        
        indeg = [0]*N
        for i in range(N):
            for node in graph[i]:
                indeg[node] += 1
        
        qu = deque()
        for i in range(N):
            if indeg[i] == 0:
                qu.append(i)
        
        ans = 0
        while qu:
            curr = qu.popleft()
            ans += 1
            
            for nei in graph[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
        
        return ans == N
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends