# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def helper(node, hei):
            if not node:
                return 0
            
            curr = None
            if node.val == p or node.val == q:
                curr = hei
            
            left = helper(node.left, hei+1)
            right = helper(node.right, hei+1)

            if left and right:
                self.ans = left+right - 2*hei
            if left and curr != None:
                self.ans = left - hei
            if right and curr != None:
                self.ans = right - hei
            
            return curr or left or right

        if p == q:
            return 0
        self.ans = 0
        helper(root, 0)
        return self.ans