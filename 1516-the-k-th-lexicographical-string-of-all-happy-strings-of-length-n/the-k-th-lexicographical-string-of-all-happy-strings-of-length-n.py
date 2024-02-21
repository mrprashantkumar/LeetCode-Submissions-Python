class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def helper(i, curr):
            if i == n:
                words.append(curr)
                return
            
            last = curr[-1]
            for ch in 'abc':
                if ch != last:
                    helper(i+1, curr+ch)
            return
        
        words = []
        for ch in 'abc':
            helper(1, ch)
        words.sort()
        return words[k-1] if len(words) >= k else ''