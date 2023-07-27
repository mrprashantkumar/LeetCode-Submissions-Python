class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def helper(k):
            time = 0
            for bat in batteries:
                time += min(bat, k)
            return time >= k*n
        
        left, right = 1, sum(batteries)//n
        while left <= right:
            mid = (left+right)//2

            if helper(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans