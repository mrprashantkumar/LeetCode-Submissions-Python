class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        d = [int(i) for i in str(num)]
        for i in d:
            if num%i==0:
                ans+=1
        return ans