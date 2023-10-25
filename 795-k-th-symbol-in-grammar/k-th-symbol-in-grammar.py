class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0
        low, high = 1, 2**(n-1)

        while low < high:
            mid = (low+high) // 2

            if k <= mid:
                high = mid
            else:
                low = mid+1
                ans = 1-ans
        
        return ans