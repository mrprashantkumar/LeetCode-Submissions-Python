# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans=[]
        qu = deque([root])
        while qu:
            n = len(qu)
            for _ in range(n):
                last = qu.popleft()
                if last.left:
                    qu.append(last.left)
                if last.right:
                    qu.append(last.right)
            ans.append(last.val)
        return ans