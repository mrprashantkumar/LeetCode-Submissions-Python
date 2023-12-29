class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def helper(i, d):
            if d < 0:
                return inf

            if i == n:
                if d == 0:
                    return 0
                return inf
            
            ans = inf
            val = -1
            for j in range(i, n):
                val = max(val, jobDifficulty[j])
                ans = min(ans, val + helper(j+1, d-1))
            
            return ans

        n = len(jobDifficulty)
        if d > n:
            return -1
        
        return helper(0, d)