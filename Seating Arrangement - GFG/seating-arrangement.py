from typing import List


class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        if m == 1 and n == 1 and seats[0] == 0:
            return True
            
        c = 0
        i = 0
        while i<m:
            if seats[i] == 1:
                break
            i += 1
        
        if i == m:
            c += (i+1)//2
        else:
            c += i//2
        
        j = m-1
        while j > i:
            if seats[j] == 1:
                break
            j -= 1
        # print(i, j, c)
        c += (m-j-1)//2
        
        while i < j:
            zero = 0
            while i < j and seats[i] == 0:
                i += 1
                zero += 1
            i += 1
            # print(zero)
            c += max(0, (zero-1)//2)
        
        return c >= n

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        seats=IntArray().Input(m)
        
        obj = Solution()
        res = obj.is_possible_to_get_seats(n, m, seats)
        
        result_val = "Yes" if res else "No"
        print(result_val)

# } Driver Code Ends