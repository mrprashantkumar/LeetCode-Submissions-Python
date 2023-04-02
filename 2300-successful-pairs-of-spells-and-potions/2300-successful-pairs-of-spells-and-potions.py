class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)
        ans = [0]*n
        
        for i in range(n):
            ind = m - bisect.bisect_left(potions, (success+spells[i]-1)//spells[i])
            ans[i] = ind
        return ans