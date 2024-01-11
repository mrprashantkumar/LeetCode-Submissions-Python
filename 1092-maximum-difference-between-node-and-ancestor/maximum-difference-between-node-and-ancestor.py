# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, mini, maxi):
            if not root:
                return 0
            
            mini = min(mini, root.val)
            maxi = max(maxi, root.val)

            lans = helper(root.left , mini, maxi)
            rans = helper(root.right, mini, maxi)

            return max(maxi-mini, lans, rans)
        
        return helper(root, root.val, root.val)