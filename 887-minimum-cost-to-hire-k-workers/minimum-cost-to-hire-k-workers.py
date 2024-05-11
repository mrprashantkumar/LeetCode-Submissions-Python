class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        pairs = [[y/x, x] for x, y in zip(quality, wage)]
        pairs.sort()
        
        qu = []
        len_qu = 0
        pref = 0
        ans = inf
        for rate, quality in pairs:
            heappush(qu, -quality)
            len_qu += 1
            pref += quality

            if len_qu > k:
                pref += heappop(qu)
                len_qu -= 1
            
            if len_qu == k:
                ans = min(ans, pref * rate)
        
        return ans