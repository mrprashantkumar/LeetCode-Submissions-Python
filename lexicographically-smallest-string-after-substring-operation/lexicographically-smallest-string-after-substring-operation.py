class Solution:
    def smallestString(self, s: str) -> str:
        arr = [i for i in s]
        n = len(arr)
        i = 0
        while i<n and arr[i] != 'a':
            i += 1
        
        if i == 0:
            while i<n and arr[i] == 'a':
                i += 1
            if i == n:
                arr[-1] = 'z'
                return "".join(arr)
            j = i
            while j<n and arr[j] != 'a':
                j += 1
            # print(i, j)
            for k in range(i, j):
                arr[k] = chr(ord(arr[k])-1)
        else:
            for k in range(i):
                arr[k] = chr(ord(arr[k])-1)
        
        return "".join(arr)
