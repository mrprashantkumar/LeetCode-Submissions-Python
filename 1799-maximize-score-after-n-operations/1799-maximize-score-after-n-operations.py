class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (1 << N)
        for bitset in range(1 << N):
            pairs = [i for i in range(N) if bitset & (1 << i)] # generate all pairs from current `bitset`
            if len(pairs) > 0 and len(pairs) % 2 == 0:
                for x_pos, y_pos in combinations(pairs, 2): # enumerate all x,y pairs
                    new_bitset = bitset ^ ((1 << x_pos) | (1 << y_pos)) 
                    dp[bitset] = max(dp[bitset], gcd(nums[x_pos], nums[y_pos]) * len(pairs) // 2 + dp[new_bitset])
        return dp[-1]