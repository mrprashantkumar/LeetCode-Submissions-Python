# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        qu = deque([root])
        ans = None
        while qu:
            ans = qu[0].val
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
        return ans