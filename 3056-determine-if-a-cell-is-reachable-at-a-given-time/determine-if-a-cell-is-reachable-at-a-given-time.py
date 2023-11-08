class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return  t != 1
        
        total = abs(sx-fx) + abs(sy-fy)
        m = min(abs(sx-fx), abs(sy-fy))
        diff = abs(abs(sx-fx) - abs(sy-fy))
        return (m+diff) <= t