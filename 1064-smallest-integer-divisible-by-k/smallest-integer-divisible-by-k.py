class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        val, ans = 1, 1
        for _ in range(k+1):
            if val % k == 0:
                return ans
            ans += 1
            val *= 10
            val += 1
        return -1