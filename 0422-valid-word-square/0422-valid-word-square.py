class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n= len(words)
        for i in range(n):
            m = len(words[i])
            for j in range(m):
                if j >= n or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True