"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        qu, clones = deque([node]), {node.val: Node(node.val, [])}
        while qu:
            cur = qu.popleft() 
            cur_clone = clones[cur.val]            

            for nei in cur.neighbors:
                if nei.val not in clones:
                    clones[nei.val] = Node(nei.val, [])
                    qu.append(nei)
                    
                cur_clone.neighbors.append(clones[nei.val])
                
        return clones[node.val]