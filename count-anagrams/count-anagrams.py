class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split()
        ans = 1
        for word in words:
            m = len(word)
            d = Counter(word)
            count = factorial(m)
            for char in d:
                count //= factorial(d[char])
            
            ans *= count
            ans %= 1000000007
        return ans