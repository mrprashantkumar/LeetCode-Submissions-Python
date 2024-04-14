# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, isleft):
            if not node:
                return 0
            
            if isleft and not node.left and not node.right:
                return node.val

            ans = dfs(node.left, True)
            ans += dfs(node.right, False)

            return ans
        
        return dfs(root, False)