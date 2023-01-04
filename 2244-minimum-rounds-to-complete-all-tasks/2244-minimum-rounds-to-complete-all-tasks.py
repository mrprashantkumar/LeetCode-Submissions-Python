class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        ans=0
        for i in d:
            if d[i]==1:
                return -1
            ans += (d[i]+2)//3
        return ans