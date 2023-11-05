class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        
        times = 0
        maxval = arr[0]

        for i in range(1, n):
            if max(maxval, arr[i]) == maxval:
                times += 1
            else:
                times = 1
                maxval = max(maxval, arr[i])
            
            if times >= k:
                return maxval
        
        return maxval