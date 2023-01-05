class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        
        flag = True
        same, diff = 0, 0
        for word in d:
            if word[0] == word[1]:
                if d[word]%2==0:
                    same += d[word]
                else:
                    same += (d[word]-1)
                    if flag:
                        same += 1
                        flag = False
            else:
                diff += min(d[word], d[word[::-1]])
        return (same+diff)*2