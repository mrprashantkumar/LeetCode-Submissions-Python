class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        qu = deque(sorted(tokens))
        ans, curr = 0, 0

        while qu and (qu[0] <= power or curr > 0):
            if qu[0] <= power:
                power -= qu.popleft()
                curr += 1
            else:
                power += qu.pop()
                curr -= 1
            ans = max(ans, curr)
        return ans