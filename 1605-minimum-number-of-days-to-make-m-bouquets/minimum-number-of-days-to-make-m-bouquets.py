class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(w):
            bouquet = 0
            curr = 0
            for day in bloomDay:
                if day <= w:
                    curr += 1
                else:
                    curr = 0
                
                if curr == k:
                    bouquet += 1
                    curr = 0
            
            return bouquet >= m
            
        n = len(bloomDay)
        if n < m*k:
            return -1
        ans = -1
        low, high = 1, max(bloomDay)

        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans