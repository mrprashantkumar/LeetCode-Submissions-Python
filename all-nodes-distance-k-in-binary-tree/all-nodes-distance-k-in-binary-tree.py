# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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

        parent = {}
        helper(root)

        qu = deque()
        qu.append(target)
        visited = set()
        visited.add(target.val)

        dist = 0
        while qu:
            res = []
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                res.append(curr.val)
                if curr.left and curr.left.val not in visited:
                    qu.append(curr.left)
                    visited.add(curr.left.val)
                
                if curr.right and curr.right.val not in visited:
                    qu.append(curr.right)
                    visited.add(curr.right.val)
                
                if curr in parent and parent[curr].val not in visited:
                    qu.append(parent[curr])
                    visited.add(parent[curr].val)

            if dist == k:
                return res
            dist += 1
        
        return []