class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []
        for i in tokens:
            if i in '+-*/':
                b = int(seen.pop())
                a = int(seen.pop())
                
                if i=='+':
                    seen.append(a+b)
                elif i=='-':
                    seen.append(a-b)
                elif i=='*':
                    seen.append(a*b)
                else:
                    seen.append(a/b)
            else:
                seen.append(i)
        
        return int(seen[0])