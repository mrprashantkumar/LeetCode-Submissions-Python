class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for j in range(2, n+1):
            for i in range(1, j):
                if math.gcd(j, i) == 1:
                    ans.append(str(i)+'/'+str(j))
        return ans