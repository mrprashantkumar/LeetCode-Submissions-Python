# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if not root:
                return ans
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
            return ans
        ans=[]
        return helper(root)