class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i
        
        ans = []
        i=0
        while i<n:
            j = i+1
            end = last[s[i]]
            while j<end:
                if last[s[j]]>end:
                    end = last[s[j]]
                j+=1
            
            ans.append(end-i+1)
            i = end+1
        return ans