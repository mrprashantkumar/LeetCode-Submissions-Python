class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        for i,j in logs:
            d[i].add(j)
        
        ans = [0]*k
        for i in d:
            ans[len(d[i])-1] += 1
        return ans