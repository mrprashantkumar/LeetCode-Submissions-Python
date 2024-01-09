# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return []
            
            ans = helper(node.left)
            if not node.left and not node.right:
                ans.append(node.val)
            ans += helper(node.right)
            return ans
        
        return helper(root1) == helper(root2)