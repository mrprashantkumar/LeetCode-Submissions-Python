class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def check(x, y):
            if x >= y:
                return True
            
            if s[x] == s[y]:
                return check(x+1, y-1)
            else:
                return False
        
        def helper(i, anssofar):
            if i == n:
                self.ans.append(anssofar)
                return
            
            for j in range(i, n):
                if check(i, j):
                    helper(j+1, anssofar + [s[i:j+1]])
            
            return

        n = len(s)
        self.ans = []
        helper(0, [])
        return self.ans