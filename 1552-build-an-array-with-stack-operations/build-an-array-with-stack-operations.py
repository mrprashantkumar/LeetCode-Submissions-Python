class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = len(target)
        val = 1
        ans = []
        i = 0
        while i < l:
            if target[i] == val:
                ans += ['Push']
                i += 1
            else:
                ans += ['Push', 'Pop']
            
            val += 1

            if val > n:
                break
        
        return ans