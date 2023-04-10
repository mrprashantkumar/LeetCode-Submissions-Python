class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for i in s:
            if i in '([{':
                seen.append(i)
            else:
                if not seen:
                    return False
                if i == ')':
                    if seen[-1] == '(':
                        seen.pop()
                    else:
                        return False
                elif i == ']':
                    if seen[-1] == '[':
                        seen.pop()
                    else:
                        return False
                elif i == '}':
                    if seen[-1] == '{':
                        seen.pop()
                    else:
                        return False
        return not seen