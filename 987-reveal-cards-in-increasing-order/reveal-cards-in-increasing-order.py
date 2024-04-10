class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        qu = deque([i for i in range(n)])

        deck.sort()
        ans = [0] * n

        for i in deck:
            ans[qu.popleft()] = i

            if qu:
                qu.append(qu.popleft())
        
        return ans