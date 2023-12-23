class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0, 0))
        x, y = 0, 0
        
        for d in path:
            if d == "N":
                y += 1
            elif d == 'E':
                x += 1
            elif d == "W":
                x -= 1
            else:
                y -= 1
            
            if (x, y) in visited:
                return True
            visited.add((x, y))
        
        return False