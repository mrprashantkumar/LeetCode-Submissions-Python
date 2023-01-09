class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        seen = []
        openB = 0
        for i in s:
            if i == '(':
                seen.append(i)
                openB += 1
                
            elif i == ')':
                if openB != 0:
                    seen.append(i)
                    openB -= 1
            else:
                seen.append(i)
        
        s = "".join(seen)
        
        seen = []
        closeB = 0
        for i in s[::-1]:
            if i == ')':
                seen.append(i)
                closeB += 1
                
            elif i == '(':
                if closeB != 0:
                    seen.append(i)
                    closeB -= 1
            else:
                seen.append(i)
        
        return "".join(seen[::-1])