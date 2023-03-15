# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        qu = deque([root])
        f = False
        
        while qu:
            curr = qu.popleft()
            if curr and f:
                return False
            
            if not curr:
                f = True
            else:
                qu.append(curr.left)
                qu.append(curr.right)
        
        return True