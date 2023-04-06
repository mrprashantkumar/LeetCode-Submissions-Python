class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def isvalid(p, q):
            return 0<=p<n and 0<=q<m and image[p][q] == initialColor and (p, q) not in visited
        
        n, m = len(image), len(image[0])
        initialColor = image[sr][sc]
        visited = set()
        
        qu = deque([(sr, sc)])
        while qu:
            x, y = qu.popleft()
            visited.add((x, y))
            image[x][y] = color
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if isvalid(x+dx, y+dy):
                    qu.append((x+dx, y+dy))
        
        return image