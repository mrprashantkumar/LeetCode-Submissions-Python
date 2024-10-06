class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        def ifPossible(source, target):
            m, n = len(target), len(source)
            if m == 1:
                return False
            
            i = 0
            while i < n and i < m:
                if source[i] == target[i]:
                    i += 1
                else:
                    break
            
            if i >= n:
                return True
            
            j1, j2 = n-1, m-1
            while j1 >= 0 and j2 >= 0:
                if source[j1] == target[j2]:
                    j1 -= 1
                    j2 -= 1
                else:
                    break
            
            if j1 < 0 or i > j1:
                return True
            
            return False

        words1 = [i for i in sentence1.split()]
        words2 = [i for i in sentence2.split()]
        n, m = len(words1), len(words2)
        if words1 == words2:
            return True
        if n < m:
            return ifPossible(words1, words2)
        else:
            return ifPossible(words2, words1)
