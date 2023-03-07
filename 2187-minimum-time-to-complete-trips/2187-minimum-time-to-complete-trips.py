class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(ans):
            count = 0
            for t in time:
                count += (ans//t)
            return count >= totalTrips
        
        low, high = 0, 100000000000007
        
        while low<high:
            mid = (low+high)//2
            
            if check(mid):
                high = mid
            else:
                low = mid+1
        return low