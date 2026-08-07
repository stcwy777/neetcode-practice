"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        org = head
        copy = Node(0)

        idx2Node = {}
        node2Idx = {}

        node = copy
        idx = 0
        while org:
            node.next = Node(org.val)

            node2Idx[org] = idx
            idx2Node[idx] = node.next

            node = node.next
            org = org.next
            idx += 1
        
        org = head
        node = copy.next

        while org:
            if org.random:
                node.random = idx2Node[node2Idx[org.random]]
            
            org = org.next
            node = node.next
        
        return copy.next
