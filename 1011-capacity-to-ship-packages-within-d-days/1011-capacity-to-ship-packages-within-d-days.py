class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(val):
            c = 1
            csum = 0
            for i in weights:
                csum += i
                if csum>val:
                    c += 1
                    csum = i
            
            return c > days
        
        low, high = max(weights), sum(weights)
        
        while low<high:
            mid = (low+high)//2
            
            if check(mid):
                low = mid+1
            else:
                high = mid
        
        return low