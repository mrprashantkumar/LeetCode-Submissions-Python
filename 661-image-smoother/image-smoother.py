class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def isvalid(p, q):
            return 0 <= p < n and 0 <= q < m
            
        def helper(x, y):
            val = 0
            count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if isvalid(x+dx, y+dy):
                        val += img[x+dx][y+dy]
                        count += 1
            
            return val // count

        n, m = len(img), len(img[0])
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = helper(i, j)
        return ans