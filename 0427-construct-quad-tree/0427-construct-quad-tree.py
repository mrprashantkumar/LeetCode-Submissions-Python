"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.build(grid, 0, 0, len(grid))
    

    def sameValue(self, grid, x, y, sideLength):
        value = grid[x][y]
        for i in range(x, x + sideLength):
            for j in range(y, y + sideLength):
                if grid[i][j] != value:
                    return False
        
        return True
    

    def build(self, grid, x, y, sideLength):
        if self.sameValue(grid, x, y, sideLength):
            return Node(grid[x][y], True)

        root = Node(0, False)
        newSideLength = sideLength // 2
        root.topLeft = self.build(grid, x, y, newSideLength)
        root.topRight = self.build(grid, x, y + newSideLength, newSideLength)
        root.bottomLeft = self.build(grid, x + newSideLength, y, newSideLength)
        root.bottomRight = self.build(grid, x + newSideLength, y + newSideLength, newSideLength)

        return root