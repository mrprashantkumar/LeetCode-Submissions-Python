# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, sumsofar):
            nonlocal ans
            if not root:
                return 
            
            sumsofar = sumsofar*10 + root.val
            if not root.left and not root.right:
                ans += sumsofar
                return 
                
            helper(root.left, sumsofar)
            helper(root.right, sumsofar)
            return 
        
        ans = 0
        helper(root, 0)
        return ans