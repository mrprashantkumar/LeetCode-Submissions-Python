class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        if 1 in d.values():
            return -1
        
        ans=0
        for i in d:
            ans += (d[i]+2)//3
        return ans