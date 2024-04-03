class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isvalid(p, q, k):
            return 0 <= p < n and 0 <= q < m and not visited[p][q] and board[p][q] == word[k]

        def helper(x, y, k):
            if k == l:
                return True
            
            if isvalid(x, y, k):
                visited[x][y] = True
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if helper(x+dx, y+dy, k+1):
                        return True
                visited[x][y] = False
            
            return False

        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        l = len(word)
        for i in range(n):
            for j in range(m):
                if helper(i, j, 0):
                    return True
        return False