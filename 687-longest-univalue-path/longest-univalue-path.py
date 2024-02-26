# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, par):
            if not node:
                return 0
            
            lans = dfs(node.left, node.val)
            rans = dfs(node.right, node.val)
            ans[0] = max(ans[0], lans+rans)

            return 1+max(lans, rans) if node.val == par else 0
            
        ans = [0]
        dfs(root, -1)
        return ans[0]