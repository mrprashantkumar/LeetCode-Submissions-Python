class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        n = len(num)
        odd, even = [], []
        temp = []
        
        for i in num:
            if int(i)&1:
                temp.append(1)
                odd.append(i)
            else:
                temp.append(0)
                even.append(i)
        
        odd.sort()
        even.sort()
        ans = ''
        for i in temp:
            if i&1:
                ans += odd.pop()
            else:
                ans += even.pop()
        return int(ans)