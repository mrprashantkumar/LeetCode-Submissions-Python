class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n+1))
        k -= 1 
        idx = k
        while n > 1:
            arr.pop(idx)
            n -= 1
            idx = (idx + k) % n
        return arr[0]