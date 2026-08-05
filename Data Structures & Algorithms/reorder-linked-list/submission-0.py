# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        N = []
        node = head.next
        while node:
            N.append(node)
            node = node.next
        
        node = head

        for i in range(len(N) // 2):
            node.next = N[len(N) - i - 1]
            N[len(N) - i - 1].next = N[i]
            node = N[i]
        
        if len(N) % 2 == 0:
            node.next = None
        else:
            node.next.next = None
