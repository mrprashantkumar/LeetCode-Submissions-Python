class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        pref = [set() for i in range(n)]
        cuts = set()
        for i in range(n):
            s = 0
            for val in wall[i]:
                s += val
                pref[i].add(s)
                cuts.add(s)
        cuts.remove(sum(wall[0]))
        
        ans = n
        for cut in cuts:
            curr = 0
            for sets in pref:
                if cut not in sets:
                    curr += 1
            ans = min(ans, curr)
        return ans