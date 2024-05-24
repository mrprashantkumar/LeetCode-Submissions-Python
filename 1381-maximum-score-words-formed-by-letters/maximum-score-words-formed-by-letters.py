class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def getscore(word, dt):
            dw = Counter(word)
            curr = 0
            for w in dw:
                if dt[w] >= dw[w]:
                    curr += dw[w] * score[ord(w) - 97]
                else:
                    return 0, dt
            
            return curr, dt - dw

        def helper(i, d):
            if i == n:
                return 0
            
            notTake = helper(i+1, d)
            sc, newD = getscore(words[i], d)
            take = 0
            if sc > 0:
                take = sc + helper(i+1, newD)

            return max(take, notTake)

        n = len(words)
        d = Counter(letters)
        return helper(0, d)