class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def findPairs(spell, plen):
            low = 0
            high = plen
            while(low <= high):
                mid = ((high - low) // 2) + low
                if(spell * potions[mid] >= success ):
                    high = mid - 1
                else:
                    low = mid +1
            return plen - low + 1
        ans = []
        potions.sort()
        for spell in spells:
            pair = findPairs(spell, len(potions) - 1)
            ans.append(pair)
        return ans