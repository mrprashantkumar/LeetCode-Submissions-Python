class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        one = s.count('1')
        zero = n - one
        
        return (one-1)*"1" + zero * ('0') + '1'