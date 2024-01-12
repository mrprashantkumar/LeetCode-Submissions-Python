class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        seen = []
        lenseen = 0
        curr = -1
        ans = []
        for i in words:
            if i == 'prev':
                if abs(curr) > lenseen:
                    ans.append(-1)
                else:
                    ans.append(seen[curr])
                    curr -= 1
            else:
                seen.append(int(i))
                lenseen += 1
                curr = -1
        
        return ans