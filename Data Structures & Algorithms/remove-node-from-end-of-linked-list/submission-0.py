# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head
        
        m = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            m += 1
        
        l = 2 * m + 1
        if fast.next:
            fast = fast.next
            l += 1
        if l == n:
            return head.next

        elif l - n > m:
            node = slow
            for _ in range(m, l - n - 1):
                node = node.next
            
            nxt = node.next.next
            node.next = nxt
        else:
            node = head
            for _ in range(l - n - 1):
                node = node.next
            nxt = node.next.next
            node.next =nxt

        return head
        