class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def helper(i, currInd):
            if i == m:
                return 0
            
            res = inf
            for pos in positions[key[i]]:
                right = abs(pos - currInd)
                left = abs(n - right)
                res = min(res, min(left, right) + helper(i+1, pos))

            return res

        n, m = len(ring), len(key)
        positions = defaultdict(list)
        for i, x in enumerate(ring):
            positions[x].append(i)
            
        return m + helper(0, 0)