# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
        
        inorder = []
        helper(root)
        ans = 1000000007
        n = len(inorder)
        for i in range(n-1):
            ans = min(ans, inorder[i+1]-inorder[i])
        return ans