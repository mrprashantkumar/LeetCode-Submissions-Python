class Solution:
    def largestPalindromic(self, num: str) -> str:
        if all(i == '0' for i in num):
            return '0'

        d = Counter(num)
        odd = -1

        ans = ''
        for i in range(9, -1, -1):
            if d[str(i)]%2 == 0:
                ans += str(i)*(d[str(i)]//2)
            else:
                ans += str(i)*((d[str(i)]-1)//2)
                if odd == -1:
                    odd = i
        
        if odd != -1:
            ans += str(odd)
            ans += ans[:-1][::-1]
        else:
            ans += ans[::-1]
        ans = ans.lstrip('0').rstrip('0')
        return ans