class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdeg, indeg = defaultdict(int), defaultdict(int)
        for x, y in paths:
            outdeg[x] += 1
            indeg[y] += 1
        
        for city in indeg:
            if city not in outdeg:
                return city
        