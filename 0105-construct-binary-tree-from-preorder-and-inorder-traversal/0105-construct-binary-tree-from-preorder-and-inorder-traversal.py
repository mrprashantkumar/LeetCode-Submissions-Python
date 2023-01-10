# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(pre, ino):
            n = len(pre)
            if n==0:
                return None
            
            root = TreeNode(pre[0])
            for i in range(n):
                if ino[i] == pre[0]:
                    ind = i
                    break
            
            root.left = helper(pre[1:ind+1], ino[:ind])
            root.right = helper(pre[ind+1:], ino[ind+1:])
            return root
        
        return helper(preorder, inorder)