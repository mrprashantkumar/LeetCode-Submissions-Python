class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        a1 = 0
        for i in range(n):  # starts zero
            if i & 1:
                if s[i] != '1':
                    a1 += 1
            else:
                if s[i] != '0':
                    a1 += 1
        
        a2 = 0
        for i in range(n):  # starts one
            if i & 1:
                if s[i] != '0':
                    a2 += 1
            else:
                if s[i] != '1':
                    a2 += 1
        
        return min(a1, a2)