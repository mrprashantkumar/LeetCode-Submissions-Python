class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u = 1,1,1,1,1

        for _ in range(n-1):
            ta, te, ti, to, tu = a, e, i, o, u
            a = te % 1000000007
            e = (ta + ti) % 1000000007
            i = (ta + te + to + tu) % 1000000007
            o = (ti + tu) % 1000000007
            u = ta % 1000000007
        
        return (a + e + i + o + u) % 1000000007