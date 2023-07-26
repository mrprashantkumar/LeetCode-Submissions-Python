class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def helper(k):
            time = 0
            for d in dist:
                if time > hour:
                    return False
                # print(k, time)
                if time != int(time):
                    time = int(time+1)
                time += d/k
            return time <= hour
        
        ans = -1
        left, right = 1, 10000007
        while left <= right:
            mid = (left+right)//2
            if helper(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans