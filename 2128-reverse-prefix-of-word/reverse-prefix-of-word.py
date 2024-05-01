class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        ind = word.index(ch)
        low, high = 0, ind
        
        ans = list(word)
        while low <= high:
            ans[low], ans[high] = ans[high], ans[low]
            low += 1
            high -= 1

        return "".join(ans)