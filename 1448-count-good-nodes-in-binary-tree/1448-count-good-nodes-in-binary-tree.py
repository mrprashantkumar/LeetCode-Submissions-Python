# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxsofar):
            nonlocal ans
            if not root:
                return
            
            if root.val >= maxsofar:
                ans += 1
            
            helper(root.left, max(maxsofar, root.val))
            helper(root.right, max(maxsofar, root.val))
        
        ans = 0
        helper(root, root.val)
        return ans