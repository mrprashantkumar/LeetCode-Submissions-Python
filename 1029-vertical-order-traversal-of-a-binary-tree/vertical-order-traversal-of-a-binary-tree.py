# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(row, col, root):
            if not root:
                return
            
            if row in d[col]:
                d[col][row].append(root.val)
                d[col][row].sort()
            else:
                d[col][row] = [root.val]
            
            helper(row + 1, col - 1, root.left)
            helper(row + 1, col + 1, root.right)
            return
        
        d = defaultdict(dict)
        helper(0, 0, root)
        mini = min(d)
        ans = []
        while mini in d:
            curr = []
            cmini = min(d[mini])
            while d[mini]:
                if cmini in d[mini]:
                    curr += d[mini][cmini]
                    del d[mini][cmini]
                cmini += 2
            ans.append(curr)
            mini += 1
        return ans