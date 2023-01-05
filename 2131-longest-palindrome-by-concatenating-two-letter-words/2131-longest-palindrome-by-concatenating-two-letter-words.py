class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        
        flag = True
        ans = 0
        for word in d:
            if word[0] == word[1]:
                if d[word]%2==0:
                    ans += d[word]
                else:
                    ans += (d[word]-1)
                    if flag:
                        ans += 1
                        flag = False
            else:
                ans += min(d[word], d[word[::-1]])
        return ans*2