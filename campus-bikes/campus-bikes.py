class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)
        dist = []
        for i in range(n):
            for j in range(m):
                dist.append([abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]), i, j])
        dist.sort()
        row, col = set(), set()
        ans = [0]*n
        co = 0
        for wt, r, c in dist:
            if r not in row and c not in col:
                ans[r] = c
                row.add(r)
                col.add(c)
                co += 1
            
            if co == n:
                return ans
        return ans