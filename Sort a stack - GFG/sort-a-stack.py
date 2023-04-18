class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        if len(s) == 0:
            return s
            
        a = s.pop()
        self.sorted(s)
        self.insertElementatPosition(a,s)
        # print(newlist)
        
    def insertElementatPosition(self,a,s):
        if len(s) == 0:
            s.append(a)
        else:
            if a>s[-1]:
                s.append(a)
            else:
                ele = s.pop()
                self.insertElementatPosition(a,s)
                s.append(ele)
        
        return s
        
    # 2 1 3  a = 3
    
    # 2 1  a = 1
    
    # 2  a = 2
    
    # []
    
    # 2
    
     
     
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends