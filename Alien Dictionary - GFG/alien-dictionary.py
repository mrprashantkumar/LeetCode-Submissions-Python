#User function Template for python3
from collections import *
class Solution:
    def findOrder(self,dict, N, K):
        graph = defaultdict(list)
        for i in range(n-1):
            for x, y in zip(dict[i], dict[i+1]):
                if x != y:
                    graph[ord(x)-97].append(ord(y)-97)
                    break
        
        indeg = [0]*K
        for i in range(k):
            for node in graph[i]:
                indeg[node] += 1
                
        qu = deque()
        for i in range(K):
            if indeg[i] == 0:
                qu.append(i)
        
        ans = []
        while qu:
            curr = qu.popleft()
            ans.append(chr(curr+97))
            for nei in graph[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    qu.append(nei)
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends