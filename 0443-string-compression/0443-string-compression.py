class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        i = 0
        n = len(chars)
        
        while i<n:
            j = i
            while j<n and chars[i]==chars[j]:
                j += 1
            
            ans.append(chars[i])
            if (j-i)>1:
                ans += [i for i in str(j-i)]
            
            i = j
        l = len(ans)
        for i in range(l):
            chars[i] = ans[i]
        return l