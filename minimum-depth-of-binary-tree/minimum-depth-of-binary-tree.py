# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        qu = deque()
        qu.append(root)
        ans = 1
        while qu:
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                if not curr.left and not curr.right:
                    return ans
                
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            ans += 1