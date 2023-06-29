class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m,n = len(grid),len(grid[0])
        totalKeys = 0
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():totalKeys += 1
                if grid[i][j]=='@':queue.append((i,j,tuple(),1))
        visited = set()
        while queue:
            i,j,keys,moves = queue.pop(0)
            if (i,j,keys) not in visited:
                visited.add((i,j,keys))
                for x,y in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]:
                    if 0<=x<m and 0<=y<n and (x,y,keys) not in visited:
                        new = set(keys)
                        if grid[x][y].islower():
                            new.add(grid[x][y])
                        if grid[x][y] in '.@' or grid[x][y].islower() or (grid[x][y].isupper() and grid[x][y].lower() in keys):
                            queue.append((x,y,tuple(new),moves+1))
                            if len(new)==totalKeys:return moves
        return -1