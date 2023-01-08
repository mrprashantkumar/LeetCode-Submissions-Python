class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<=2:
            return n
        
        def getSlope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1==x2:
                return 1000000007
            return (y2-y1)/(x2-x1)
            
        ans = 1
        for i in range(n):
            d = defaultdict(int)
            for j in range(i+1, n):
                slope = getSlope(points[i], points[j])
                d[slope] += 1
                ans = max(d[slope], ans)
        return ans+1
                    