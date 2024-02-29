# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        qu = deque()
        qu.append(root)
        while qu:
            curr = []
            l = len(qu)
            for _ in range(l):
                node = qu.popleft()
                curr.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            ans.append(curr)
        return ans[::-1]