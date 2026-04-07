# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        switch_node = head.next
        prev_node = head
        while switch_node is not None:
            nxt_node = switch_node.next
            switch_node.next = prev_node

            prev_node = switch_node
            switch_node = nxt_node
        head.next = None

        return prev_node
            