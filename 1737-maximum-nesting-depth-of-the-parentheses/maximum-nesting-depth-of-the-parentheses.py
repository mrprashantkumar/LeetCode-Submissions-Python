class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        op = 0
        for i in s:
            if i == '(':
                op += 1
            elif i == ')':
                op -= 1
            ans = max(ans, op)
        return ans