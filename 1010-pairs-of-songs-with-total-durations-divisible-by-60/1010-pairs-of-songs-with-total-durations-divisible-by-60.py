class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        
        for i in time:
            i %= 60
            if (60-i)%60 in d:
                ans += d[(60-i)%60]
            d[i] += 1
        
        return ans