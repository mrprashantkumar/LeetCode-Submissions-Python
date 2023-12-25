class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def helper(i):
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0
            
            ans = 0
            if s[i] == '*':
                ans +=  9 * helper(i+1)
            else:
                ans += helper(i+1)

            if i+1 < n:
                if s[i] == '1':
                    if '0' <= s[i+1] <= '9':
                        ans += helper(i+2)
                    elif s[i+1] == '*':
                        ans += 9 * helper(i+2)

                elif s[i] == '2':
                    if '0' <= s[i+1] <= '6':
                        ans += helper(i+2)
                    elif s[i+1] == '*':
                        ans += 6 * helper(i+2)
                
                elif s[i] == '*':
                    if '0' <= s[i+1] <= '6':
                        ans += 2 * helper(i+2)
                    elif '7' <= s[i+1] <= '9':
                        ans += helper(i+2)
                    elif s[i+1] == '*':
                        ans += 15 * helper(i+2)

            return ans % 1000000007
        
        n = len(s)
        return helper(0)