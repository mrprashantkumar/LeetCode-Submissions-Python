class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        row = [0]*n
        col = [0]*m
        
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B":
                    row[i] += 1
                    col[j] += 1
        # print(row, col)
        ans = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B" and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans