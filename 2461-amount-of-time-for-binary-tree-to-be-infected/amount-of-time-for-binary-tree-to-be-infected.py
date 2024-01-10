# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def helper(node):
            if not node:
                return 
            
            if node.left:
                parent[node.left] = node
                helper(node.left)
            
            if node.right:
                parent[node.right] = node
                helper(node.right)
            
            return
        
        def find(node):
            if not node:
                return
            if node.val == start:
                return node
            return find(node.left) or find(node.right)
        
        parent = {}
        helper(root)

        qu = deque()
        qu.append(find(root))
        visited = set()
        visited.add(start)

        ans = -1
        while qu:
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()

                if curr.left and curr.left.val not in visited:
                    qu.append(curr.left)
                    visited.add(curr.left.val)
                
                if curr.right and curr.right.val not in visited:
                    qu.append(curr.right)
                    visited.add(curr.right.val)
                
                if curr in parent and parent[curr].val not in visited:
                    qu.append(parent[curr])
                    visited.add(parent[curr].val)
            
            ans += 1
        
        return ans