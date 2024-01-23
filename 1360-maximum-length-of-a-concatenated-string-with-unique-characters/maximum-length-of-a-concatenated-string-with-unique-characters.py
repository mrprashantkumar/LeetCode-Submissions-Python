class Solution:
    def maxLength(self, arr: List[str]) -> int:
        @cache
        def helper(i, charsofar):
            allUnique = False
            l = len(charsofar)
            if len(set(charsofar)) == l:
                allUnique = True
                self.ans = max(self.ans, l)
            
            if i == n or not allUnique:
                return
            
            for j in range(i, n):
                helper(j+1, charsofar+arr[j])
            
            return 
        
        n = len(arr)
        self.ans = 0
        helper(0, '')
        return self.ans