class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(i, anssofar):
            if i == n:
                ans.add(anssofar)
                return
            
            helper(i+1, '()'+anssofar)
            l = len(anssofar)
            for j in range(l//2 + 1):
                helper(i+1, anssofar[:j]+'()'+anssofar[j:])
            
            return
        
        ans = set()
        helper(0, '')
        return list(ans)