# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0, 0
            
            leftsum, leftcount = helper(node.left)
            rightsum, rightcount = helper(node.right)

            if leftcount == 0 and rightcount == 0:
                self.ans += 1
            elif (leftsum + rightsum + node.val) // (leftcount + rightcount + 1) == node.val:
                self.ans += 1
            
            return (leftsum + rightsum + node.val), (leftcount + rightcount + 1)
        
        self.ans = 0
        helper(root)
        return self.ans