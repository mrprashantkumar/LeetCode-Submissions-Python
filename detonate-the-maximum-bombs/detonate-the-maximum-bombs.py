class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def withinReach(a, b, c, d, r):
            dist = (a-c)*(a-c) + (b-d)*(b-d)
            return dist <= r*r

        def bfs(coordinate, toBeChecked):
            x, y, r = coordinate
            qu = deque()
            qu.append(coordinate)
            ans = 0
            while qu:
                x, y, r = qu.pop()
                ans += 1
                temp = []
                toberemoved = set()
                for a, b, r2 in toBeChecked:
                    if withinReach(x, y, a, b, r):
                        qu.append((a, b, r2))
                    else:
                        temp.append([a, b, r2])
                toBeChecked = temp
            return ans
        
        n = len(bombs)
        res = 0
        for i in range(n):
            smans = bfs(bombs[i], bombs[:i]+bombs[i+1:])
            res = max(res, smans)
        return res