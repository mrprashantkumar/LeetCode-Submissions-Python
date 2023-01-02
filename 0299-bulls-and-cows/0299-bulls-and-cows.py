class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1, d2 = {}, {}
        x, y = 0, 0
        for i, j in zip(secret, guess):
            if i == j:
                x+=1
            else:
                d1[i] = d1.get(i, 0)+1
                d2[j] = d2.get(j, 0)+1
        
        for i in d1:
            y += min(d1.get(i, 0), d2.get(i, 0))
        
        return str(x)+"A"+str(y)+"B"