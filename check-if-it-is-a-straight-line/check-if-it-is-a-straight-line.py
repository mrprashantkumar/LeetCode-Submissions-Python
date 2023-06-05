class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        for i in range(n-2):
            a, b = coordinates[i]
            c, d = coordinates[i+1]
            e, f = coordinates[i+2]
            if (d-b)*(e-c) != (f-d)*(c-a):
                return False
        return True