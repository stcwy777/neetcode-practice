"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        root = None
        if not node:
            return root
        
        root = Node(node.val)
        nodes = deque([node])
        node_hash = {node.val: root}

        while nodes:
            for _ in range(len(nodes)):
                cur_node = nodes.pop()
                
                # if cur_node.val not in node_hash:
                #     new_node = Node(cur_node.val)
                #     node_hash[new_node.val] = new_node
                
                # assign_neighbors = True if node_hash[cur_node.val].neighbors == [] else False 
            
                for n in cur_node.neighbors:
                    if n.val not in node_hash:
                        nodes.append(n)                        
                        new_node = Node(n.val)
                        node_hash[n.val] = new_node
                    # if assign_neighbors:
                    node_hash[cur_node.val].neighbors.append(node_hash[n.val])

        return root

        
