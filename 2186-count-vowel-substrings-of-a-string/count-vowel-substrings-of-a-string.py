class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        ans = 0
        d = Counter()
        left = 0
        start = 0
        for right in range(n):
            if word[right] in 'aeiou':
                d[word[right]] += 1
                while len(d) >= 5:
                    d[word[left]] -= 1
                    if d[word[left]] == 0:
                        del d[word[left]]
                    left += 1
                
                ans += (left - start)
            else:
                d = Counter()
                start = right+1
                left = right+1
            
        return ans