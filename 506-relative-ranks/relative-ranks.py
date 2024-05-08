class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        for i, x in enumerate(score):
            d[x] = i
        
        n = len(score)
        ans = [0] * n
        score.sort()

        for i in range(n):
            curr = score.pop()
            if i == 0:
                ans[d[curr]] = "Gold Medal"
            elif i == 1:
                ans[d[curr]] = "Silver Medal"
            elif i == 2:
                ans[d[curr]] = "Bronze Medal"
            else:
                ans[d[curr]] = str(i+1)

        return ans