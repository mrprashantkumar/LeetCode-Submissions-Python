class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def helper(k):
            count = 1
            last = position[0]
            for i in range(1, n):
                if position[i] - last >= k:
                    count += 1
                    last = position[i]
                
                if count == m:
                    return True
            
            return count >= m
        
        position.sort()
        n = len(position)
        low, high = 1, 10**9
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans