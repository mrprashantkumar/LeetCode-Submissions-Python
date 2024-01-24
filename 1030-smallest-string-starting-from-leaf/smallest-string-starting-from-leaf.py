# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node, path):
            if not node:
                return 
            
            if not node.left and not node.right:
                self.ans = min(self.ans, chr(node.val + 97) + path)
                return 
            
            helper(node.left, chr(node.val + 97) + path)
            helper(node.right, chr(node.val + 97) + path)
            return 
        
        self.ans = 'z'*8501
        helper(root, '')
        return self.ans