# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getLCA(node):
            if not node:
                return None
            if node in nodes:
                return node
            left = getLCA(node.left)
            right = getLCA(node.right)
            if left and right:
                return node
            else:
                return left or right

        qu = deque([root])
        while qu:
            l = len(qu)
            deepest = []
            for _ in range(l):
                curr = qu.popleft()
                deepest.append(curr)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
        
        nodes = set(deepest)
        return getLCA(root)
