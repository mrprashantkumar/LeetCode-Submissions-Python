class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdeg, indeg = set(), set()
        for x, y in paths:
            outdeg.add(x)
            indeg.add(y)
        
        for city in indeg:
            if city not in outdeg:
                return city
        