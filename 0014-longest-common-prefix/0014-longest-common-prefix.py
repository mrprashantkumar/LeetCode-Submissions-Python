class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        l = len(min(strs))
        i=0
        base = strs[0]
        while i<l:
            for word in strs:
                if word[i] != base[i]:
                    return ans
            ans+=base[i]
            i+=1
        
        return ans