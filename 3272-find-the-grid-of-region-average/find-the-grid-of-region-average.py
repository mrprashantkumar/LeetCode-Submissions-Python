class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def isvalid(p, q):
            for x in range(p, p+3):
                for y in range(q, q+3):
                    for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                        if p <= x+dx < p+3 and q <= y+dy < q+3:
                            if abs(image[x][y] - image[x+dx][y+dy]) > threshold:
                                return False
            return True

        n, m = len(image), len(image[0])
        ans = [[0]*m for _ in range(n)]
        count = [[0]*m for _ in range(n)]

        for i in range(n-2):
            for j in range(m-2):
                if isvalid(i, j):
                    val = 0
                    for x in range(i, i+3):
                        for y in range(j, j+3):
                            val += image[x][y]
                    val //= 9

                    for x in range(i, i+3):
                        for y in range(j, j+3):
                            count[x][y] += 1
                            ans[x][y] += val
        
        for i in range(n):
            for j in range(m):
                if count[i][j] == 0:
                    ans[i][j] = image[i][j]
                else:
                    ans[i][j] //= count[i][j]
        return ans