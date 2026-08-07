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

        nodeMap = {}
        node = copy

        while org:
            node.next = Node(org.val)

            nodeMap[org] = node.next
            node = node.next
            org = org.next

        org = head
        node = copy.next

        while org:
            if org.random:
                node.random = nodeMap[org.random]
            
            org = org.next
            node = node.next
        
        return copy.next
