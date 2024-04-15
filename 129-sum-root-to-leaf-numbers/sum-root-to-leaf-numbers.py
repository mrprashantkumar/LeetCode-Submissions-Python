# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, sumsofar):
            if not root:
                return 0
            
            sumsofar = sumsofar*10 + root.val
            if not root.left and not root.right:
                return sumsofar
                
            return helper(root.left, sumsofar) + helper(root.right, sumsofar)
                    
        return helper(root, 0)