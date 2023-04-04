#User function Template for python3

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        words = set(wordList)
        m = len(startWord)
        qu = deque([(startWord, [startWord])])
        
        
        ans = []
        while qu:
            # print(qu)
            l = len(qu)
            used = set()
            f = False
            for _ in range(l):
                curr, pathsofar = qu.popleft()
                for i in range(m):
	                for j in range(97, 123):
	                    word = curr[:i]+chr(j)+curr[i+1:]
	                    if word in words:
    	                    if word == targetWord:
    	                        f = True
    	                        ans.append(pathsofar+[word])
    	                    else:
    	                        qu.append([word, pathsofar+[word]])
    	                        used.add(word)
    	   # print(used, words)
    	    while used:
    	        words.remove(used.pop())
    	    if f:
    	        break
    	
    	return ans


#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends