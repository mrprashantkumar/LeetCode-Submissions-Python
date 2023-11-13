class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        temp = []
        flag = [False]*n
        ans = ''
        
        for i, ch in enumerate(s):
            if ch in 'aeiouAEIOU':
                temp.append(ch)
                flag[i] = True
        
        temp.sort()
        j = 0
        for i in range(n):
            if flag[i]:
                ans += temp[j]
                j += 1
            else:
                ans += s[i]
        
        return ans