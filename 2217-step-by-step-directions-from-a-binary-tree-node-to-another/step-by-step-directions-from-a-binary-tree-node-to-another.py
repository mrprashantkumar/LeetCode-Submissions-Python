# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def traverse(node):
            if not node:
                return None
            lnode, rnode = None, None
            if node.left:
                parent[node.left] = node
                lnode = traverse(node.left)
            if node.right:
                parent[node.right] = node
                rnode = traverse(node.right)
            if node.val == startValue:
                return node
            return lnode or rnode
        
        parent = {}
        start = traverse(root)
        qu = deque()
        qu.append([start, ''])
        visited = set()
        visited.add(start)
        while qu:
            l = len(qu)
            for _ in range(l):
                node, path = qu.popleft()
                if node.val == destValue:
                    return path
                
                if node.left and node.left not in visited:
                    qu.append((node.left, path+'L'))
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    qu.append((node.right, path+'R'))
                    visited.add(node.right)
                if node in parent and parent[node] not in visited:
                    qu.append((parent[node], path+'U'))
                    visited.add(parent[node])