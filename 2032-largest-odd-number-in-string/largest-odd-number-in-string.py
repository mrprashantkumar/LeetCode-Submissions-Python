class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ''
        odd = '13579'
        n = len(num)
        for i in range(n):
            if num[i] in odd:
                ans = num[:i+1]
        return ans