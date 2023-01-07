# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0, True
            
            lh, ls = helper(root.left)
            rh, rs = helper(root.right)
            
            if not ls or not rs or abs(lh-rh)>1:
                return 0, False
            
            return 1+max(lh, rh), True
        
        return helper(root)[1]