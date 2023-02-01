class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        if str1 + str2 != str2 + str1:
            return ""
        
        s1, s2 = len(str1), len(str2)
        ans = math.gcd(s1, s2)
        return str1[:ans]
        