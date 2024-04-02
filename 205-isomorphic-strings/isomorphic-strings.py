class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        for x, y in zip(s, t):
            if x in ds and ds[x] != y:
                return False
            else:
                ds[x] = y
        
        dt = {}
        for x, y in zip(t, s):
            if x in dt and dt[x] != y:
                return False
            else:
                dt[x] = y
        
        return True