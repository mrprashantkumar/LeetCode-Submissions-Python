from collections import *
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
	    words = set(wordList)
	    m = len(startWord)
	    qu = deque([startWord])
	    ans = 1
	    while qu:
	       # print(qu)
	        l = len(qu)
	        for _ in range(l):
	            curr = qu.popleft()
	            for i in range(m):
	                for j in range(97, 123):
	                    word = curr[:i]+chr(j)+curr[i+1:]
	                    if word in words:
    	                    if word == targetWord:
    	                        return ans+1
    	                    else:
    	                        qu.append(word)
    	                        words.remove(word)
    	    ans += 1
	    return 0


#{ 
 # Driver Code Starts
from collections import deque 
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
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends