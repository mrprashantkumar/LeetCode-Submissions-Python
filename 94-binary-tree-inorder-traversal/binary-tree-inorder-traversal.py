# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)
        
        self.ans = []
        dfs(root)
        return self.ans