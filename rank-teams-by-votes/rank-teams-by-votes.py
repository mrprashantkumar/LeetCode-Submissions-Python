class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = defaultdict(lambda: [0] * 26)

        for vote in votes:
            for i, x in enumerate(vote):
                count[x][i] -= 1
        # print(count)
        ans = sorted(count.items(), key = lambda x : (x[1], x[0]))
        return "".join(a[0] for a in ans)