# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def find(node, l=0, r=0):
            if node:
                res[0] = max(res[0], l, r)
                find(node.left, 0, l+1)
                find(node.right, r+1, 0)
            
        res = [0]
        find(root)
        return res[0]