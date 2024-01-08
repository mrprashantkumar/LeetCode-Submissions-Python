# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, low, high):
            if not root:
                return 0
                
            ans = 0
            if root.val < low:
                ans += helper(root.right, low, high)
            elif root.val > high:
                ans += helper(root.left, low, high)
            else:
                ans += helper(root.left, low, high)
                ans += root.val
                ans += helper(root.right, low, high)
            
            return ans
        
        return helper(root, low, high)

            
