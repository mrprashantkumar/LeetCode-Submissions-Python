# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, path):
            nonlocal ans
            if not root:
                return
            
            if not root.left and not root.right:
                path += str(root.val)
                ans.append(path)
                return 
            
            helper(root.left, path+str(root.val)+"->")
            helper(root.right, path+str(root.val)+"->")
            return
        
        ans = []
        helper(root, "")
        return ans