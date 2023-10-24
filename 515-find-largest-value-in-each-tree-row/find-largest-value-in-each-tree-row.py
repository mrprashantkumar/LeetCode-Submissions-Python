# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        qu = deque([root])
        while qu:
            n = len(qu)
            rowMax = -inf
            for _ in range(n):
                curr = qu.popleft()
                rowMax = max(rowMax, curr.val)

                if curr.left: qu.append(curr.left)
                if curr.right: qu.append(curr.right)

            ans.append(rowMax)

        return ans