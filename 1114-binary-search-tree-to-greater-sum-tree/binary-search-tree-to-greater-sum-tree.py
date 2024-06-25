# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node:
                return
            
            helper(node.right)
            node.val += self.total
            self.total = node.val
            helper(node.left)
            return 
        
        self.total = 0
        helper(root)
        return root