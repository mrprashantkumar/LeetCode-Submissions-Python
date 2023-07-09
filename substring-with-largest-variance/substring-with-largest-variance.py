class Solution:
    def largestVariance(self, s: str) -> int:
        def getMaxVariance(c1, c2):
            count1, count2 = 0, 0
            rem2 = d[c2]
            res = 0
            for ch in s:
                if ch == c1:
                    count1 += 1
                elif ch == c2:
                    count2 += 1
                    rem2 -= 1
                    
                if count2 > 0:
                    res = max(res, count1 - count2)
                if count2 > count1 and rem2 > 0:
                    count1, count2 = 0, 0
            return res

        
        n = len(s)
        if len(set(s)) == 1 or len(set(s)) == n:
            return 0
        
        d = Counter(s)
        ans = 0
        for i in d:
            for j in d:
                if i != j:
                    ans = max(ans, getMaxVariance(i, j))
        return ans