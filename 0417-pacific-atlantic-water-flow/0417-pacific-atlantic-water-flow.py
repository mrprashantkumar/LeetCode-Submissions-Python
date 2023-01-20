class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < rows and 0 <= y < cols:
                    if matrix[x][y] >= matrix[i][j]:
                        traverse(x, y, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)