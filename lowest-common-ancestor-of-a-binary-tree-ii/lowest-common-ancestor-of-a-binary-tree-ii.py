# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ispresent(node, target):
            if not node:
                return False
            if node.val == target.val:
                return True
            return ispresent(node.left, target) or ispresent(node.right, target)
        
        def getLCA(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = getLCA(node.left)
            right = getLCA(node.right)
            if left and right:
                return node
            else:
                return left or right

        if not ispresent(root, p) or not ispresent(root, q):
            return None
        
        return getLCA(root)