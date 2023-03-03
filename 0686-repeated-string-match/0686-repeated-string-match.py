class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        
        r = math.ceil(m//n)
        
        if b in a*r:
            return r
        if b in a*(r+1):
            return r+1
        if b in a*(r+2):
            return r+2
        return -1