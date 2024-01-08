# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if not root:
                return 0

            ans = 0
            if root.val < low:
                ans += helper(root.right)
            elif root.val > high:
                ans += helper(root.left)
            else:
                ans += helper(root.left)
                ans += root.val
                ans += helper(root.right)
            
            return ans
        
        return helper(root)