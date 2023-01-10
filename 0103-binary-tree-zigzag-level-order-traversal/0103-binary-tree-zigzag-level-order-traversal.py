# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans=[]
        level = 1
        qu = deque([root])
        while qu:
            n = len(qu)
            arr = []
            for _ in range(n):
                curr = qu.popleft()
                arr.append(curr.val)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            if level&1:
                ans.append(arr)
            else:
                ans.append(arr[::-1])
            level+=1
        return ans