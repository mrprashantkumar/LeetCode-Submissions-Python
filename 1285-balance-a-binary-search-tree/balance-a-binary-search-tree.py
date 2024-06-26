# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def constructBST(low, high):
            if low <= high:
                mid = (low+high) //2
                node = TreeNode(self.inorder[mid])
                node.left = constructBST(low, mid-1)
                node.right = constructBST(mid+1, high)
                return node
            
            return None

        def getInorder(node):
            if node:
                getInorder(node.left)
                self.inorder.append(node.val)
                getInorder(node.right)
        
        self.inorder = []
        getInorder(root)
        n = len(self.inorder)
        return constructBST(0, n-1)