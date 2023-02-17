# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.cur = None 
        self.minimum = float('inf')
        def inorder(node):
            if node:
                inorder(node.left)
                if self.cur:
                    self.minimum = min(self.minimum,node.val-self.cur.val)
                self.cur = node
                # res.append(node.val)
                inorder(node.right)
        inorder(root)
        return self.minimum