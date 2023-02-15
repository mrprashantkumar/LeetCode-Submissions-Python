class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        
        carry = 0
        for i in range(n-1, -1, -1):
            num[i] += (carry + k%10)
            carry = num[i]//10
            num[i] %= 10
            k //= 10
        
        carry += k
        while carry>0:
            num.insert(0, carry%10)
            carry //= 10
            
        return num