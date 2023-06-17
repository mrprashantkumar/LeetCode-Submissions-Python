class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        def dfs(i, prev):
            if i == n:
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]

            cost = 1000000007
            
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])
            
            idx = bisect.bisect_right(arr2, prev)
            
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            dp[(i, prev)] = cost
            return cost
        
        dp = {}
        arr2.sort()
        n = len(arr1)
        res = dfs(0, -1)
        return res if res != 1000000007 else -1