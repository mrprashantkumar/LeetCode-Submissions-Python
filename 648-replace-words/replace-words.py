class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        ans = []
        words = [i for i in sentence.split()]

        for word in words:
            f = True
            for i, x in enumerate(word):
                if word[:i+1] in d:
                    ans.append(word[:i+1])
                    f = False
                    break
            if f:
                ans.append(word)
            
        return " ".join(ans)