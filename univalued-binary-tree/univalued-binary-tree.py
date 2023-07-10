# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        qu = deque()
        qu.append(root)
        while qu:
            curr = qu.popleft()
            if curr.val != root.val:
                return False
            
            if curr.left:
                qu.append(curr.left)
            if curr.right:
                qu.append(curr.right)
        return True