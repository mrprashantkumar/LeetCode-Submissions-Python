# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root:
            return ans
        ans.append(root.val)
        qu = deque([root])
        while qu:
            n = len(qu)
            rowMax = -math.inf
            for _ in range(n):
                curr = qu.popleft()
                if curr.left:
                    rowMax = max(rowMax, curr.left.val)
                    qu.append(curr.left)
                if curr.right:
                    rowMax = max(rowMax, curr.right.val)
                    qu.append(curr.right)
            ans.append(rowMax)
        return ans[:-1]
            
            