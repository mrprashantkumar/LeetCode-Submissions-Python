# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        qu = deque()
        qu.append(root)

        while qu:
            depth -= 1
            if depth == 1:
                l = len(qu)
                for _ in range(l):
                    curr = qu.popleft()
                    currLeft, currRight = curr.left, curr.right

                    newLeft, newRight = TreeNode(val), TreeNode(val)

                    curr.left, curr.right = newLeft, newRight

                    newLeft.left, newRight.right = currLeft, currRight

            else:
                l = len(qu)
                for _ in range(l):
                    curr = qu.popleft()
                    if curr.left:
                        qu.append(curr.left)
                    if curr.right:
                        qu.append(curr.right)
        
        return root