class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(time):
            count = 0
            for i in piles:
                count += (i+time-1)//time
            
            return count <= h
        
        low, high = 1, 1000000007
        
        while low<high:
            mid = (low+high)//2
            
            if check(mid):
                high = mid
            else:
                low = mid+1
        return low