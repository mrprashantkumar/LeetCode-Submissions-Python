class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = Counter(deck)
        val = 0
        for i in d:
            val = gcd(val, d[i])
        if val == 1:
            return False
        return all(d[i]%val == 0 for i in d)