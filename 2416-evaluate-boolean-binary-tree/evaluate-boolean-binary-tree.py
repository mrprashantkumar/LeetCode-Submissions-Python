# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        if not root.left and not root.right:
            return root.val
        
        if root.val==2:
            return self.evaluateTree(root.left) | self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) & self.evaluateTree(root.right)