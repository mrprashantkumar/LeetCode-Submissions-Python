class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        ans = 0
        n = 0
        nums = sorted(d.keys(), key=lambda x : d[x], reverse = True)
        for i in nums:
            n += 1
            
            if n <= 8:
                ans += d[i] * 1
            elif n <= 16:
                ans += d[i] * 2
            elif n <= 24:
                ans += d[i] * 3
            else:
                ans += d[i] * 4
            
        return ans