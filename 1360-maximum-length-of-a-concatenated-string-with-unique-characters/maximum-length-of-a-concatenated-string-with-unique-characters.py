class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def helper(i, charsofar):
            allUnique = False
            l = len(charsofar)
            if len(set(charsofar)) == l:
                allUnique = True
                self.ans = max(self.ans, l)
            
            if i == n or not allUnique:
                return
            
            helper(i+1, charsofar)
            helper(i+1, charsofar+arr[i])
            return 
        
        n = len(arr)
        self.ans = 0
        helper(0, '')
        return self.ans