class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        qu = deque([i for i in range(n+1)])

        ans = []
        for i in s:
            if i == 'I':
                ans.append(qu.popleft())
            else:
                ans.append(qu.pop())
        ans.append(qu.pop())
        return ans