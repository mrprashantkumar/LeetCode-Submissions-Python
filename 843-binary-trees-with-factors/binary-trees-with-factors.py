class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        dp = {}

        for i in range(n):
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    dp[arr[i]] += dp[arr[j]] * dp.get(arr[i] // arr[j], 0)
                    dp[arr[i]] %= 1000000007
        
        return sum(dp.values()) % 1000000007