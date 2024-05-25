class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def ispossible(i):
            if i == n:
                return True

            for j in range(i, n):
                if s[i:j+1] in words:
                    if ispossible(j+1):
                        return True
            
            return False

        def helper(i, anssofar):
            if i == n:
                ans.append(' '.join(anssofar))
                return
            
            for j in range(i, n):
                if s[i:j+1] in words:
                    helper(j+1, anssofar + [s[i:j+1]])
            return 

        words = set(wordDict)
        n = len(s)
        ans = []
        if ispossible(0):
            helper(0, [])
        return ans